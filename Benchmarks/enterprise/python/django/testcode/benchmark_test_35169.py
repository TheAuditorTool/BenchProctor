# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35169(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
