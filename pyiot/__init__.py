# -*- coding: UTF-8 -*-

import pyiot.pyiot


def get_pyiot(host, qq, log_level="INFO", socketio_logger=False):
    return pyiot.pyiot(host, qq, log_level=log_level, socketio_logger=socketio_logger)
