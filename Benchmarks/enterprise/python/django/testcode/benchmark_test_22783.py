# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22783(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
