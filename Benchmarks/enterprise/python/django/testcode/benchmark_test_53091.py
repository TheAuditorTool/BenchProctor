# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest53091(request):
    xml_value = request.body.decode('utf-8')
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
