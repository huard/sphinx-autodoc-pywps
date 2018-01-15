# -*- coding: utf-8 -*-
from sphinx.ext.autodoc import ClassDocumenter
from sphinx.ext.napoleon.docstring import NumpyDocstring
from sphinx.util.docstrings import prepare_docstring
from sphinx.util import force_decode
from six import text_type
import pywps
from pywps.app.Common import Metadata

class ProcessDocumenter(ClassDocumenter):
    """Sphinx autodoc ClassDocumenter subclass that understands the 
    pywps.Process class. 
    
    The Process description, its inputs and docputs are converted to a 
    numpy style docstring. Additional sections (Notes, References, 
    Examples, etc.) can be added in the Process subclass docstring. 
    """
    priority = ClassDocumenter.priority+1
    
    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return issubclass(cls, pywps.Process)
        
    def fmt_type(self, obj):
        """Input and output type formatting (type, default and allowed
        values).
        """
        nmax = 10
        
        doc = ''
        try:
            if getattr(obj, 'allowed_values', None):
                av = ', '.join(["'{}'".format(i.value) for i in obj.allowed_values[:nmax]])
                if len(obj.allowed_values) > nmax:
                    av += ', ...'

                doc += " : {" + av + "}"

            elif getattr(obj, 'data_type', None):
                doc += ' : ' + obj.data_type

            elif getattr(obj, 'data_format', None):
                doc += ' : ' + obj.data_format.mime_type

            if getattr(obj, 'min_occurs', None) is not None:
                if obj.min_occurs == 0:
                    doc += ', optional'
                    if getattr(obj, 'default', None) :
                        doc += ':{0}'.format(obj.default)

        except Exception as e:
            raise type(e)(e.message + ' in {0} docstring'.format(self.object().identifier))
        return doc


    def make_doc(self):
        """Numpy style docstring where meta data is scraped from the 
        class instance.
        
        The numpy style is used because it supports multiple outputs.
        """
        obj = self.object()
        
        # Description
        doc = []
        doc.append(u"``{}`` {} (v{})".format(obj.identifier,  obj.title, obj.version or '',))
        doc.append('')
        doc.append(obj.abstract)
        doc.append('')
        
        # Inputs
        doc.append('Parameters')
        doc.append('----------')
        for i in obj.inputs:
            doc.append("{}{}".format(i.identifier, self.fmt_type(i)))
            doc.append("   {}".format( i.abstract or i.title))
        doc.append('')    
        
        # Outputs
        doc.append("Returns")
        doc.append("-------")
        for i in obj.outputs:
            doc.append("{}{}".format(i.identifier, self.fmt_type(i)))
            doc.append("   {}".format( i.abstract or i.title))
        doc.append('')    
        
        # Metadata
        isref = False
        ref = []
        ref.append("References")
        ref.append("----------")
        ref.append('')
        for m in obj.metadata:
            if isinstance(m, Metadata):
                title, href = m.title, m.href
            elif type(m) == dict:
                title, href = m['title'], m['href']
            else:
                title, href = None, None
            if title and href:    
                ref.append(u" - `{} <{}>`_".format(title, href))
                isref = True
                
        ref.append('')
        
        if isref: 
            doc += ref

        return doc
        return u'\n'.join(doc)
        
                                      

    def get_doc(self, encoding=None, ignore=1):
        """Overrides ClassDocumenter.get_doc to create the doc scraped from the Process object, then adds additional
        content from the class docstring.
        """

        process_docstring = self.make_doc()
        class_docstring = self.get_attr(self.object, '__doc__', [])

        if class_docstring:
            process_docstring.append(class_docstring)

        docstrings = NumpyDocstring(process_docstring, what='class').lines()

        doc = []
        for docstring in docstrings:
            if isinstance(docstring, text_type):
                doc.append(prepare_docstring(docstring, ignore))
            elif isinstance(docstring, str):  # this will not trigger on Py3
                doc.append(prepare_docstring(force_decode(docstring, encoding),
                                             ignore))
        return doc


def setup(app):
    app.add_autodocumenter(ProcessDocumenter)
