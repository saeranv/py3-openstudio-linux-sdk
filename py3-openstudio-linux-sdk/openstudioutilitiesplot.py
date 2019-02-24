# This file was automatically generated by SWIG (http://www.swig.org).

# Version 3.0.7

#

# Do not make changes to this file unless you know what you are doing--modify

# the SWIG interface file instead.











from sys import version_info

if version_info >= (2, 6, 0):

    def swig_import_helper():

        from os.path import dirname

        import imp

        fp = None

        try:

            fp, pathname, description = imp.find_module('_openstudioutilitiesplot', [dirname(__file__)])

        except ImportError:

            import _openstudioutilitiesplot

            return _openstudioutilitiesplot

        if fp is not None:

            try:

                _mod = imp.load_module('_openstudioutilitiesplot', fp, pathname, description)

            finally:

                fp.close()

            return _mod

    _openstudioutilitiesplot = swig_import_helper()

    del swig_import_helper

else:

    import _openstudioutilitiesplot

del version_info

try:

    _swig_property = property

except NameError:

    pass  # Python < 2.2 doesn't have 'property'.





def _swig_setattr_nondynamic(self, class_type, name, value, static=1):

    if (name == "thisown"):

        return self.this.own(value)

    if (name == "this"):

        if type(value).__name__ == 'SwigPyObject':

            self.__dict__[name] = value

            return

    method = class_type.__swig_setmethods__.get(name, None)

    if method:

        return method(self, value)

    if (not static):

        if _newclass:

            object.__setattr__(self, name, value)

        else:

            self.__dict__[name] = value

    else:

        raise AttributeError("You cannot add attributes to %s" % self)





def _swig_setattr(self, class_type, name, value):

    return _swig_setattr_nondynamic(self, class_type, name, value, 0)





def _swig_getattr_nondynamic(self, class_type, name, static=1):

    if (name == "thisown"):

        return self.this.own()

    method = class_type.__swig_getmethods__.get(name, None)

    if method:

        return method(self)

    if (not static):

        return object.__getattr__(self, name)

    else:

        raise AttributeError(name)



def _swig_getattr(self, class_type, name):

    return _swig_getattr_nondynamic(self, class_type, name, 0)





def _swig_repr(self):

    try:

        strthis = "proxy of " + self.this.__repr__()

    except:

        strthis = ""

    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)



try:

    _object = object

    _newclass = 1

except AttributeError:

    class _object:

        pass

    _newclass = 0





try:

    import weakref

    weakref_proxy = weakref.proxy

except:

    weakref_proxy = lambda x: x





class SwigPyIterator(_object):

    __swig_setmethods__ = {}

    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)

    __swig_getmethods__ = {}

    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)



    def __init__(self, *args, **kwargs):

        raise AttributeError("No constructor defined - class is abstract")

    __repr__ = _swig_repr

    __swig_destroy__ = _openstudioutilitiesplot.delete_SwigPyIterator

    __del__ = lambda self: None



    def value(self) -> "PyObject *":

        return _openstudioutilitiesplot.SwigPyIterator_value(self)



    def incr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":

        return _openstudioutilitiesplot.SwigPyIterator_incr(self, n)



    def decr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":

        return _openstudioutilitiesplot.SwigPyIterator_decr(self, n)



    def distance(self, x: 'SwigPyIterator') -> "ptrdiff_t":

        return _openstudioutilitiesplot.SwigPyIterator_distance(self, x)



    def equal(self, x: 'SwigPyIterator') -> "bool":

        return _openstudioutilitiesplot.SwigPyIterator_equal(self, x)



    def copy(self) -> "swig::SwigPyIterator *":

        return _openstudioutilitiesplot.SwigPyIterator_copy(self)



    def next(self) -> "PyObject *":

        return _openstudioutilitiesplot.SwigPyIterator_next(self)



    def __next__(self) -> "PyObject *":

        return _openstudioutilitiesplot.SwigPyIterator___next__(self)



    def previous(self) -> "PyObject *":

        return _openstudioutilitiesplot.SwigPyIterator_previous(self)



    def advance(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":

        return _openstudioutilitiesplot.SwigPyIterator_advance(self, n)



    def __eq__(self, x: 'SwigPyIterator') -> "bool":

        return _openstudioutilitiesplot.SwigPyIterator___eq__(self, x)



    def __ne__(self, x: 'SwigPyIterator') -> "bool":

        return _openstudioutilitiesplot.SwigPyIterator___ne__(self, x)



    def __iadd__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":

        return _openstudioutilitiesplot.SwigPyIterator___iadd__(self, n)



    def __isub__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":

        return _openstudioutilitiesplot.SwigPyIterator___isub__(self, n)



    def __add__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":

        return _openstudioutilitiesplot.SwigPyIterator___add__(self, n)



    def __sub__(self, *args) -> "ptrdiff_t":

        return _openstudioutilitiesplot.SwigPyIterator___sub__(self, *args)

    def __iter__(self):

        return self

SwigPyIterator_swigregister = _openstudioutilitiesplot.SwigPyIterator_swigregister

SwigPyIterator_swigregister(SwigPyIterator)





_openstudioutilitiesplot.SHARED_PTR_DISOWN_swigconstant(_openstudioutilitiesplot)

SHARED_PTR_DISOWN = _openstudioutilitiesplot.SHARED_PTR_DISOWN

from .import openstudioutilitiesdata

from .import openstudioutilitiestime

from .import openstudioutilitiescore

from .import openstudioutilitiesunits

class ProgressBar(_object):

    __swig_setmethods__ = {}

    __setattr__ = lambda self, name, value: _swig_setattr(self, ProgressBar, name, value)

    __swig_getmethods__ = {}

    __getattr__ = lambda self, name: _swig_getattr(self, ProgressBar, name)

    __repr__ = _swig_repr



    def __init__(self, *args):

        if self.__class__ == ProgressBar:

            _self = None

        else:

            _self = self

        this = _openstudioutilitiesplot.new_ProgressBar(_self, *args)

        try:

            self.this.append(this)

        except:

            self.this = this

    __swig_destroy__ = _openstudioutilitiesplot.delete_ProgressBar

    __del__ = lambda self: None



    def minimum(self) -> "int":

        return _openstudioutilitiesplot.ProgressBar_minimum(self)



    def setMinimum(self, min: 'int') -> "void":

        return _openstudioutilitiesplot.ProgressBar_setMinimum(self, min)



    def maximum(self) -> "int":

        return _openstudioutilitiesplot.ProgressBar_maximum(self)



    def setMaximum(self, max: 'int') -> "void":

        return _openstudioutilitiesplot.ProgressBar_setMaximum(self, max)



    def value(self) -> "int":

        return _openstudioutilitiesplot.ProgressBar_value(self)



    def windowTitle(self) -> "std::string":

        return _openstudioutilitiesplot.ProgressBar_windowTitle(self)



    def text(self) -> "std::string":

        return _openstudioutilitiesplot.ProgressBar_text(self)



    def isVisible(self) -> "bool":

        return _openstudioutilitiesplot.ProgressBar_isVisible(self)



    def setVisible(self, visible: 'bool') -> "void":

        return _openstudioutilitiesplot.ProgressBar_setVisible(self, visible)



    def onPercentageUpdated(self, percentage: 'double') -> "void":

        return _openstudioutilitiesplot.ProgressBar_onPercentageUpdated(self, percentage)



    def setRange(self, min: 'int', max: 'int') -> "void":

        return _openstudioutilitiesplot.ProgressBar_setRange(self, min, max)



    def setValue(self, value: 'int') -> "void":

        return _openstudioutilitiesplot.ProgressBar_setValue(self, value)



    def setWindowTitle(self, *args) -> "void":

        return _openstudioutilitiesplot.ProgressBar_setWindowTitle(self, *args)

    def __disown__(self):

        self.this.disown()

        _openstudioutilitiesplot.disown_ProgressBar(self)

        return weakref_proxy(self)

ProgressBar_swigregister = _openstudioutilitiesplot.ProgressBar_swigregister

ProgressBar_swigregister(ProgressBar)



# This file is compatible with both classic and new-style classes.





