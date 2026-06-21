# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest04016():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
