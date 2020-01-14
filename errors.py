class Error:
    type: str = ""
    massage: str = ""
    def __init__(self, *args):
        self.massage = self.massage.formater(*args)
        string = "{}: "+self.massage.format(self.type)
        print(string)

class PathError(Error):
    type: str = "PathError"
    massage: str = "path {} not found"
