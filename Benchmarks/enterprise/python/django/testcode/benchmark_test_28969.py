# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


def coalesce_blank(value):
    return value or ''

def BenchmarkTest28969(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = coalesce_blank(cookie_value)
    eval(compile('with open(\'plugins/generated_config.py\', \'w\') as fh:\n    fh.write(\'SETTING = "\' + str(data) + \'"\')\nrunpy.run_path(\'plugins/generated_config.py\')', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
