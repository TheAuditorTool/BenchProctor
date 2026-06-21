# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest51109():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
