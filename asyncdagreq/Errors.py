class Unauthorized(Exception):
    def __init__(self, message: str = 'Err: 403 Unauthorized Token'):
        super(Unauthorized, self).__init__(message)


class Filenotappropriate(Exception):
    def __init__(self, message: str = 'ERR: 415 File found was not of the Appropriate image type'):
        super(Filenotappropriate, self).__init__(message)


class Largeimg(Exception):
    def __init__(self, message: str = 'ERR: 413 Image supplied was too large to be processed'):
        super(Largeimg, self).__init__(message)


class ProcessError(Exception):
    def __init__(self, message: str = 'ERR: 422 Unable to process the image due to an Error'):
        super(ProcessError, self).__init__(message)


class Connection(Exception):
    def __init__(self,
                 message: str = 'ERR: 400 Unable to connect to image url within timeout or Your ImageUrl is badly '
                                'frames'):
        super(Connection, self).__init__(message)


class ERROR502(Exception):
    def __init__(self,
                 message: str = 'ERR: 502 Bad Gateway Error'):
        super(ERROR502, self).__init__(message)