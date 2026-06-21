# SPDX-License-Identifier: Apache-2.0
import tempfile
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00421():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
