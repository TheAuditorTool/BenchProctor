# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08924(request):
    xml_value = request.body.decode('utf-8')
    divisor = int(str(xml_value)) if str(xml_value).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
