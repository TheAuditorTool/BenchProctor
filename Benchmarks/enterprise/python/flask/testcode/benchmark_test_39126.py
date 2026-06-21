# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest39126():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
