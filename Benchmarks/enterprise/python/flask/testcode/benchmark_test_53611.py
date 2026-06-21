# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def coalesce_blank(value):
    return value or ''

def BenchmarkTest53611():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = coalesce_blank(forwarded_ip)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
