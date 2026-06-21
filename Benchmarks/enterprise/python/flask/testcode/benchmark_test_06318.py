# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest06318():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
