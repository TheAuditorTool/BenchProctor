# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest63475():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
