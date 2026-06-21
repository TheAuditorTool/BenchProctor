# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from urllib.parse import unquote
from flask import request


def BenchmarkTest00109():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    return Markup('<div>' + str(data) + '</div>')
