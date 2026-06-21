# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from urllib.parse import unquote
from flask import request


def BenchmarkTest43411():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
