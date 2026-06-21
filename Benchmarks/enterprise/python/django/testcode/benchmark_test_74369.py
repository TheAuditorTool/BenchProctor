# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74369(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
