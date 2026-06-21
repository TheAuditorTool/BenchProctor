# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12493(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
