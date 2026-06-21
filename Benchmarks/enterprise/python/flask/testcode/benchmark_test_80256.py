# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest80256():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
