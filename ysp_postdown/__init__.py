import sys
from .ctor import MDDoc
from .parser import parse

if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')
    
__author__ = 'YangShuiPing'
__version__ = '1.0.2'

