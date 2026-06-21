# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os


def BenchmarkTest44786():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
