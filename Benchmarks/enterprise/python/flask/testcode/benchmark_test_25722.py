# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest25722():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
