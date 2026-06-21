# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07473(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    processed = 'true' if str(origin_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
