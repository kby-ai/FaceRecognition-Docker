import os

from ctypes import *
from numpy.ctypeslib import ndpointer
from facebox import FaceBox

libPath = os.path.abspath(os.path.dirname(__file__)) + '/libfacesdk2.so'
facesdk = cdll.LoadLibrary(libPath)

getMachineCode = facesdk.getMachineCode
getMachineCode.argtypes = []
getMachineCode.restype = c_char_p

setActivation = facesdk.setActivation
setActivation.argtypes = [c_char_p]
setActivation.restype = c_int32

initSDK = facesdk.initSDK
initSDK.argtypes = [c_char_p]
initSDK.restype = c_int32

faceDetection = facesdk.faceDetection
faceDetection.argtypes = [ndpointer(c_ubyte, flags='C_CONTIGUOUS'), c_int32, c_int32, POINTER(FaceBox), c_int32]
faceDetection.restype = c_int32

templateExtraction = facesdk.templateExtraction
templateExtraction.argtypes = [ndpointer(c_ubyte, flags='C_CONTIGUOUS'), c_int32, c_int32, POINTER(FaceBox)]
templateExtraction.restype = c_int32

similarityCalculation = facesdk.similarityCalculation
similarityCalculation.argtypes = [c_ubyte * 2048, c_ubyte * 2048]
similarityCalculation.restype = c_float
