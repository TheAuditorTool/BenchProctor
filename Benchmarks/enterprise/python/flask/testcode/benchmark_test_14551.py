# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14551():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
