# -*- coding: utf-8 -*-

"""
VideoCapture Example.

* Run this file.
"""

import wpf
from System.Windows import Application, Window
from example_videocapture_viewmodel import ExampleVideoCapureViewmodel
from opencvsharp import *

class Example_databinding_main(Window):

    def __init__(self):
        self.vm = ExampleVideoCapureViewmodel()
        self.DataContext = self.vm
        wpf.LoadComponent(self, 'example_videocapture_view.xaml')
        print('Init window.')

if __name__ == '__main__':
    Application().Run(Example_databinding_main())

