# SPDX-License-Identifier: Apache-2.0
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest35426(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
