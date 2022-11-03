# Sébastien Deriaz
# 03.11.2022
#
# Syndesi ID wrapper

from .libsyndesi import LibSyndesi

class SyndesiID:
    def __init__(self, libsyndesi : LibSyndesi, descriptor : str):
        """
        Create a new syndesi ID

        Parameters
        ----------
        libsyndesi : LibSyndesi
            Syndesi library wrapper
        descriptor : str
            ID descriptor (needs documentation)
        """
        self._lib = libsyndesi._lib
        # Create a new SyndesiID
        self._pid = self._lib.newSyndesiID()

        b_descriptor = descriptor.encode('utf-8')

        if self._lib.syndesiIDParseDescriptor(self._pid, b_descriptor):
            # Success !
            pass
        else:
            raise ValueError(f"Couldn't parse descriptor : \"{descriptor}\"")

    def __str__(self) -> str:
        raw_string = self._lib.syndesiIDString(self._pid)
        return raw_string.decode('utf-8')

    def __del__(self):
        self._lib.delSyndesiID(self._pid)





    