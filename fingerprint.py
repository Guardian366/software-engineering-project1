#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.
"""

import time
from pyfingerprint.pyfingerprint import PyFingerprint


class Scanner:

    def __init__(self):
        self.scanner = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    def enrollFingerprint(self):
        ## Enrolls new finger
        ## Tries to initialize the sensor
        positionNumber = -1
        try:
            self.scanner = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            if ( self.scanner.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))

        ## Gets some sensor information
        print('Currently used templates: ' + str(self.scanner.getTemplateCount()) +'/'+ str(self.scanner.getStorageCapacity()))

        ## Tries to enroll new finger
        try:
            print('Waiting for finger...')

            ## Wait that finger is read
            while ( self.scanner.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            self.scanner.convertImage(0x01)

            ## Checks if finger is already enrolled
            result = self.scanner.searchTemplate()
            positionNumber = result[0]

            if ( positionNumber >= 0 ):
                print('Template already exists at position #' + str(positionNumber))
                exit(0)

            print('Remove finger...')
            time.sleep(2)

            print('Waiting for same finger again...')

            ## Wait that finger is read again
            while ( self.scanner.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 2
            self.scanner.convertImage(0x02)

            ## Compares the charbuffers
            if ( self.scanner.compareCharacteristics() == 0 ):
                raise Exception('Fingers do not match')

            ## Creates a template
            self.scanner.createTemplate()

            ## Saves template at new position number
            positionNumber = self.scanner.storeTemplate()
            print('Finger enrolled successfully!')
            print('New template position #' + str(positionNumber))

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))

        return positionNumber




    def searchFinger(self):
        ## Search for a finger
        ## Tries to initialize the sensor
        positionNumber = -1
        try:
            self.scanner = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            if ( self.scanner.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('The fingerprint sensor could not be initialized!')
            print('Exception message: ' + str(e))

        ## Gets some sensor information
        print('Currently used templates: ' + str(self.scanner.getTemplateCount()) +'/'+ str(self.scanner.getStorageCapacity()))

        ## Tries to search the finger and calculate hash
        try:
            print('Waiting for finger...')

            ## Wait that finger is read
            while ( self.scanner.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            self.scanner.convertImage(0x01)

            ## Searchs template
            result = self.scanner.searchTemplate()

            positionNumber = result[0]
            accuracyScore = result[1]

            if ( positionNumber == -1 ):
                return positionNumber
            else:
                return positionNumber
        except:
            return positionNumber
