# SPDX-License-Identifier: Apache-2.0
import requests


def BenchmarkTest68684(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
