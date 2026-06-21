# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request


@dataclass
class FormData:
    payload: str

def BenchmarkTest51237():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
