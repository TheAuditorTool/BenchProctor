# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07015(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return Markup('<img src="' + str(data) + '">')
