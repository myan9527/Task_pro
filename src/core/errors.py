# -*- coding: utf-8 -*-

class StandardWebError(Exception):
    '''
    Standard error thrown by web framework
    '''
    def __init__(self, error, data='', message=''):
        super(StandardWebError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class InvalidValueError(StandardWebError):
    def __init__(self,field,message=''):
        super(StandardWebError,self).__init__('Invalid value', field, message)  
        
class ResourceNotFoundError(StandardWebError):
    def __init__(self,field,message=''):
        super(StandardWebError,self).__init__('Not found value', field, message)

class PermissionError(StandardWebError):
    def __init__(self,field,message=''):
        super(StandardWebError,self).__init__('Permission not allowed',field,message)