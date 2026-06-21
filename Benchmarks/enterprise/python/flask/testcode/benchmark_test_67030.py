# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest67030():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
