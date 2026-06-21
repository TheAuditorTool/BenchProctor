# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33838(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
