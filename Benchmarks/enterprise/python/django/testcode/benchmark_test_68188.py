# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68188(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value}'
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
