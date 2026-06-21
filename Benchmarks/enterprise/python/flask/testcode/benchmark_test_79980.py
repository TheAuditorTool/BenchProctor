# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest79980():
    user_id = request.args.get('id', '')
    data = normalise_input(user_id)
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
