# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def coalesce_blank(value):
    return value or ''

def BenchmarkTest01609():
    multipart_value = request.form.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
