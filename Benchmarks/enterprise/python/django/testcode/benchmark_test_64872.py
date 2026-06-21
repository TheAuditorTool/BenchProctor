# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64872(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
