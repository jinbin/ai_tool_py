import pathlib

class utils:
    @classmethod
    def getDataDir(self, file):
        # joinpath 不能使用 "/../../data"
        # 需要加上return 才有返回值
        return str(pathlib.Path(__file__).parent.absolute().joinpath("../../data/" + file))