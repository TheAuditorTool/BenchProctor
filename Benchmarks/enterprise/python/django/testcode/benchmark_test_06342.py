# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06342(request):
    xml_value = request.body.decode('utf-8')
    try:
        int(str(xml_value))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
