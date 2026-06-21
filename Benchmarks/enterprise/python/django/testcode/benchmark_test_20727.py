# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20727(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
