# SPDX-License-Identifier: Apache-2.0
import requests


def BenchmarkTest49497(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
