import ctypes

#interopabililty
d = ctypes.cdll.LoadLibrary(r'Z:\___advanced python\TestDll.dll')
# configure that the func return double
d.doubleFunc.restype = ctypes.c_double
# make sure the parameter is double as the function in c++
print(d.doubleFunc(ctypes.c_double(1.23)))

