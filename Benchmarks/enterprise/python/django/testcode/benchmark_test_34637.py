# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34637(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
