# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17041(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
