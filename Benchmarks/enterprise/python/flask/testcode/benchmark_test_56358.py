# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import defusedxml.ElementTree


@dataclass
class FormData:
    payload: str

def BenchmarkTest56358(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
