import abi

__m = abi.load("script.module.cffi", "_cffi_backend")
import sys
sys.modules[__name__]  = __m
