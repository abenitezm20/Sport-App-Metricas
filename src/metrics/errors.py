class ApiError(Exception):
    code = 500
    description = 'Server error'

class SqsError(ApiError):
    def __init__(self, msg, http_code=500):
        super.__init__(msg)
        self.code = http_code
        self.description = msg