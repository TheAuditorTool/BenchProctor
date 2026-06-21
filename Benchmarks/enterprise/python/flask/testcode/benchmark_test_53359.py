# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest53359(path_param):
    path_value = path_param
    data = handle(path_value)
    eval(compile('tree = etree.fromstring(b\'<users><user name="admin"/></users>\')\ntree.xpath(\'/users/user[name="\' + str(data) + \'"]\')', '<sink>', 'exec'))
    return jsonify({"result": "success"})
