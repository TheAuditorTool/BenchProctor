# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest57128():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
