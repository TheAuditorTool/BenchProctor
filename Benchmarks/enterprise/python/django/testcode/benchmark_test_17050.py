# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17050(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ' '.join(str(forwarded_ip).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
