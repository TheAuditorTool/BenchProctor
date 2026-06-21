# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from urllib.parse import urlparse
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest52579(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return jsonify({'error': 'forbidden host'}), 403
    target_url = data
    return redirect(str(target_url))
