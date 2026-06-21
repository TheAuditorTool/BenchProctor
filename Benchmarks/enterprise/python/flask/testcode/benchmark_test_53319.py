# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest53319():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    return Markup('<div>' + str(data) + '</div>')
