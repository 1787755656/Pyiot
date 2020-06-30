# -*- coding: UTF-8 -*-

import time


class SimpleLogger:
    def __init__(self):
        self.level = 2

    @staticmethod
    def __get_date():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def set_level(self, level):
        if level == "DEBUG":
            self.level = 1
        elif level == "INFO":
            self.level = 2
        elif level == "WARNING":
            self.level = 3
        elif level == "ERROR":
            self.level = 4
        elif level == "FATAL":
            self.level = 5
        else:
            raise ValueError('"level" must be one of ["DEBUG", "INFO", "WARNING", "ERROR", "FATAL"]')

    def printer(self, level, tag="default", *args):
        text = " ".join(args)
        print("{} - {} - [{}] - {}".format(self.__get_date(), level, tag, text))

    def debug(self, tag, *args):
        if self.level <= 1:
            self.printer("DEBUG", tag, *args)

    def info(self, tag, *args):
        if self.level <= 2:
            self.printer("INFO", tag, *args)

    def warning(self, tag, *args):
        if self.level <= 3:
            self.printer("WARNING", tag, *args)

    def error(self, tag, *args):
        if self.level <= 4:
            self.printer("ERROR", tag, *args)

    def fatal(self, tag, *args):
        if self.level <= 5:
            self.printer("FATAL", tag, *args)
