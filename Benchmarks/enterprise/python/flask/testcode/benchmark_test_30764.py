# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import os
import tempfile


@dataclass
class FormData:
    payload: str

def BenchmarkTest30764():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
