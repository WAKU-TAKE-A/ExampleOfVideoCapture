# -*- coding: utf-8 -*-

"""
ViewModel.
"""

import clr
from livet import *
from opencvsharp import *

class ExampleVideoCapureViewmodel(ViewModel):

    def __init__(self):
        # StartGrab command.
        self.StartGrabCommand = ViewModelCommand(self.StartGrab)
        # StopGrab command.
        self.StopGrabCommand = ViewModelCommand(self.StopGrab)
        # Init command.
        self.InitCommand = ViewModelCommand(self.Init)
        # Close command.
        self.CloseCommand = ViewModelCommand(self.Close)
        # var.
        self.vid = OpenCvSharp.VideoCapture()
        self.vid.FrameWidth = self.ImageWidth
        self.vid.FrameHeight = self.ImageHeight
        self.isGrab = False  

    #
    # DelegateCommand
    #

    def Init(self):
        print("Run ExampleVideoCapureViewmodel.Init.")

    def Close(self):
        print("Run ExampleVideoCapureViewmodel.Close.")
        self.isGrab = False
        Cv2.DestroyAllWindows()

    def StartGrab(self):
        self.vid.Release()
        self.vid.Open(self.DeviceNo)
        self.vid.FrameWidth = self.ImageWidth
        self.vid.FrameHeight = self.ImageHeight
        mat = Mat()
        self.isGrab = True
        while self.isGrab:
            ret = self.vid.Read(mat)
            Cv2.ImShow("Grab", mat)
            Cv2.WaitKey(1) # To refresh the display properly, run it.
            Cv2Util.DoEvents()

    def StopGrab(self):
        self.isGrab = False

    #
    # NotificationProperty
    #

    # ImageWidth notification property.
    _ImageWidth = 640
    @property
    def ImageWidth(self):
        return self._ImageWidth
    @ImageWidth.setter
    def ImageWidth(self, value):
        if self._ImageWidth == value:
            return
        self._ImageWidth = value
        self.RaisePropertyChanged('')
    
    # ImageHeight notification property.
    _ImageHeight = 480
    @property
    def ImageHeight(self):
        return self._ImageHeight
    @ImageHeight.setter
    def ImageHeight(self, value):
        if self._ImageHeight == value:
            return
        self._ImageHeight = value
        self.RaisePropertyChanged('')
    
    # DeviceNo notification property.
    _DeviceNo = 0
    @property
    def DeviceNo(self):
        return self._DeviceNo
    @DeviceNo.setter
    def DeviceNo(self, value):
        if self._DeviceNo == value:
            return
        self._DeviceNo = value
        self.RaisePropertyChanged('')