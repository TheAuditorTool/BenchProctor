# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def BenchmarkTest74540():
    user_id = request.args.get('id', '')
    return Markup('<div>' + str(user_id) + '</div>')
