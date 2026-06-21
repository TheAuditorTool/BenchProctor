# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest61202():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
