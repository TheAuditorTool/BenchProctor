# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30630(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
