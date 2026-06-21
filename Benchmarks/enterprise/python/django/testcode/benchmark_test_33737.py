# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33737(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
