# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23833(request):
    xml_value = request.body.decode('utf-8')
    if xml_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = xml_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
