# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40759(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
