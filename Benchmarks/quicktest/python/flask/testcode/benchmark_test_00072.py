# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest00072():
    host_value = request.headers.get('Host', '')
    data = normalise_input(host_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
