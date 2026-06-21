# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os


def BenchmarkTest10364():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
