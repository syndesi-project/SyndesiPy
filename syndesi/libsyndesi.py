# Sébastien Deriaz
# 03.11.2022
#
# Syndesi C++ interface

from ctypes import *
from os.path import dirname, join

SYNDESI_LIB_PATH = join(dirname(__file__), "../../Syndesi/libSyndesi.so")


class LibSyndesi:
    def __init__(self):
        """
        Instanciate the Syndesi library
        """
        self._lib = CDLL(SYNDESI_LIB_PATH)
        self._set_types()
        
        # Instanciate the core
        self._pcore = self._lib.newCore()
        print(self._pcore)

    def _set_types(self):
        """
        Set C++ functions output types
        """
        # void* newCore()
        self._lib.newCore.restype = c_void_p
        self._lib.newCore.argtypes = []
        # void delCore(void*)
        self._lib.delCore.restype = None
        self._lib.newCore.argtypes = [c_void_p]
        # void* newSyndesiID()
        self._lib.newSyndesiID.restype = c_void_p
        self._lib.newCore.argtypes = []
        # void delSyndesiID(void* ID)
        self._lib.delSyndesiID.restype = None
        self._lib.delSyndesiID.argtypes = [c_void_p]
        # bool syndesiIDParseDescriptor(void* ID, const char* descriptor)
        self._lib.syndesiIDParseDescriptor.restype = c_bool
        self._lib.syndesiIDParseDescriptor.argtypes = [c_void_p, c_char_p]
        # const char* syndesiIDString(void* ID)
        self._lib.syndesiIDString.restype = c_char_p
        self._lib.syndesiIDString.argtypes = [c_void_p]



    def __del__(self):
        """
        Delete the class and free the syndesi core
        """
        self._lib.delCore(self._pcore)    