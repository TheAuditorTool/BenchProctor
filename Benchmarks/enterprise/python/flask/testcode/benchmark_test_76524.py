# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest76524():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    eval(compile('tree = etree.fromstring(b\'<users><user name="admin"/></users>\')\ntree.xpath(\'/users/user[name="\' + str(data) + \'"]\')', '<sink>', 'exec'))
    return jsonify({"result": "success"})
