# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
import sys
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest35919():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = FormData(payload=argv_value).payload
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
