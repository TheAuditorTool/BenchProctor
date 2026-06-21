# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08920(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
