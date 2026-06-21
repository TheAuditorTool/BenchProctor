# SPDX-License-Identifier: Apache-2.0
import requests


def BenchmarkTest65912(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
