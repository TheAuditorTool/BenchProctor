# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def BenchmarkTest32223():
    user_id = request.args.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
