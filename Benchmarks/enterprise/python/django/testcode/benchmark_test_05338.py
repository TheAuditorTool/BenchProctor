# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05338(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
