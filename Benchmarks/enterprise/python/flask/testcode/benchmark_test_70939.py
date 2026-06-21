# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest70939():
    ua_value = request.headers.get('User-Agent', '')
    data = coalesce_blank(ua_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
