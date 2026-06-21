# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest12825():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
