# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13287(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
