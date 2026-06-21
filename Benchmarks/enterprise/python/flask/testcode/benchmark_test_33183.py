# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request
import os


def BenchmarkTest33183():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
