import os

import diskcache
import platformdirs

from guidance.llms.caches import Cache


class DiskCache(Cache):
    """DiskCache is a cache that uses diskcache lib."""
    def _init_(self, llm_name: str):
        cache_dir = (
            "/tmp"
            if "AWS_EXECUTION_ENV" in os.environ
            else platformdirs.user_cache_dir("guidance")
        )
        self._diskcache = diskcache.Cache(
            os.path.join(cachedir, f"{llm_name}.diskcache")
        )

    def __getitem__(self, key: str) -> str:
        return self._diskcache[key]

    def __setitem__(self, key: str, value: str) -> None:
        self._diskcache[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self._diskcache
    
    def clear(self):
        self._diskcache.clear()
