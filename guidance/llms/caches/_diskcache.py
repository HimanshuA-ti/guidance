import os

import diskcache
import platformdirs

from guidance.llms.caches import Cache


class DiskCache(Cache):
    """DiskCache is a cache that uses diskcache lib."""
    def __init__(self, llm_name: str):
        print("Inside my guidance")
        print(llm_name)
        cache_dir = "/tmp/cache/"+ f"{llm_name}.diskcache"
        print(cache_dir)
        self._diskcache = diskcache.Cache(
            cache_dir
        )

    def __getitem__(self, key: str) -> str:
        return self._diskcache[key]

    def __setitem__(self, key: str, value: str) -> None:
        self._diskcache[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self._diskcache
    
    def clear(self):
        self._diskcache.clear()
