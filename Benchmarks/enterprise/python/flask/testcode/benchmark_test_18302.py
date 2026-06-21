# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest18302():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
