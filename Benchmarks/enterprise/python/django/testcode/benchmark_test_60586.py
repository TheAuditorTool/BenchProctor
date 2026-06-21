# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60586(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = forwarded_ip if forwarded_ip else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
