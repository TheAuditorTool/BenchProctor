# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest48473(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
