class Logger:
    def __init__(self, verbose, cursor='> '):
        self.verbose = verbose
        self.cursor = cursor
        self.formatting = {
            "header": "\033[95m",
            "info": "\033[94m",
            "ok": "\033[92m",
            "warning": "\033[93m",
            "fail": "\033[91m",
            "end": "\033[0m",
            "bold": "\033[1m",
            "underline": "\033[4m"
        }

    def __log_general(self, form: str, string: str):
        if self.verbose:
            print(f'{form}{self.cursor}{string}{self.formatting["end"]}')

    def log(self, string: str):
        self.__log_general(self.formatting['ok'], string)

    def log_warning(self, string: str):
        self.__log_general(self.formatting['warning'], string)

    def log_error(self, string: str):
        self.__log_general(self.formatting['fail'], string)

    def log_underline(self, string: str):
        self.__log_general(self.formatting['underline'], string)

    def log_bold(self, string: str):
        self.__log_general(self.formatting['bold'], string)

    def log_info(self, string: str):
        self.__log_general(self.formatting['info'], string)
