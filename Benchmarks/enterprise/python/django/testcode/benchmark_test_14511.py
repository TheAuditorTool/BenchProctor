# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import runpy


request_state: dict[str, str] = {}

def BenchmarkTest14511(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    eval(compile('with open(\'plugins/generated_config.py\', \'w\') as fh:\n    fh.write(\'SETTING = "\' + str(data) + \'"\')\nrunpy.run_path(\'plugins/generated_config.py\')', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
