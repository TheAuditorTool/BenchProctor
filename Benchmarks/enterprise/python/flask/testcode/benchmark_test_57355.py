# SPDX-License-Identifier: Apache-2.0
import requests


def BenchmarkTest57355(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
