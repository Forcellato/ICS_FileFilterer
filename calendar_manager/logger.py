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
        """
        Function used to print on the terminal custom messages
        :param form: format of the message, like the color or if it is underlined
        :param string: message that needs to be printed
        """
        if self.verbose:
            print(f'{form}{self.cursor}{string}{self.formatting["end"]}')

    def log(self, string: str):
        """
        This function prints a given message in the default green style
        :param string: message that needs to be printed
        """
        self.__log_general(self.formatting['ok'], string)

    def log_warning(self, string: str):
        """
        This function prints a given message in the default warning style
        :param string: message that needs to be printed
        """
        self.__log_general(self.formatting['warning'], string)

    def log_error(self, string: str):
        """
        This function prints a given message in the default error style
        :param string: message that needs to be printed
        """
        self.__log_general(self.formatting['fail'], string)

    def log_underline(self, string: str):
        """
        This function prints a given message in the underlined style
        :param string: message that needs to be printed
        """
        self.__log_general(self.formatting['underline'], string)

    def log_bold(self, string: str):
        """
        This function prints a given message in the default bold style
        :param string: message that needs to be printed
        """
        self.__log_general(self.formatting['bold'], string)

    def log_info(self, string: str):
        """
        This function prints a given message in the default info style
        :param string: message that needs to be printed
        """
        self.__log_general(self.formatting['info'], string)
