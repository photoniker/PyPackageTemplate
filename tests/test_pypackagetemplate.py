from pypackagetemplate import __version__
from pypackagetemplate.pypackagetemplate import PyPackageTemplate


def test_version():
    assert __version__ == "0.1.0"


def test_public_method():
    ins = PyPackageTemplate()
    v = 1
    assert v == ins.public_method(v)


def test_add_vars():
    ins = PyPackageTemplate()
    v1 = 4
    v2 = 6
    assert 10 == ins.add_vars(v1, v2)
