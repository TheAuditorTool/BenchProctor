# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os


def BenchmarkTest78317():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
