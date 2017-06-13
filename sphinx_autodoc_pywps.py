import inspect

from sphinx.ext.autodoc import FunctionDocumenter, MethodDocumenter, ClassDocumenter
from sphinx.util.docstrings import prepare_docstring
import pywps

class ProcessDocumenter(ClassDocumenter):
    priority = ClassDocumenter.priority+1
    
    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return issubclass(cls, pywps.Process)
        
    def make_numpy_doc(self):
        """Numpy style docstring (supports multiple outputs)."""
        out = []
        obj = self.object()
        
        out.append("{} *{}* : {}".format(obj.identifier, obj.version, obj.title))
        out.append('')
        out.append(obj.abstract)
        out.append('')
        out.append('Parameters')
        out.append('----------')
        
        for i in obj.inputs:
            if getattr(i, 'data_type', None):
                out.append("{} : {}".format(i.identifier, i.data_type))
            else:
                out.append("{}".format(i.identifier))
            out.append("   {}".format( getattr(i, 'abstract', None) or getattr(i, 'title', '')))
        
        out.append('')    
        out.append("Returns")
        out.append("-------")
        for i in obj.outputs:
            if getattr(i, 'data_type', None):
                out.append("{} : {}".format(i.identifier, i.data_type))
            else:
                out.append("{}".format(i.identifier))
            out.append("   {}".format( getattr(i, 'abstract', None) or getattr(i, 'title', '')))
        
        
        result = [prepare_docstring('\n'.join(out))]
        return result

    def get_doc(self, *args, **kwds):
        # Scrape the information from the Process instance.
        doc = self.make_numpy_doc()
        
        # Get extra sections from the class docstring
        extra = super(ProcessDocumenter, self).get_doc(*args, **kwds) 
        
        out = doc + extra
        return out[-2:]


def setup(app):
    app.add_autodocumenter(ProcessDocumenter)
