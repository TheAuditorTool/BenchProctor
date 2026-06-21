# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46831(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % str(forwarded_ip)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
