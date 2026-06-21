# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80777(request):
    xml_value = request.body.decode('utf-8')
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
