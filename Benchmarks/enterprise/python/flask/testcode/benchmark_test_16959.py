# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest16959(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
