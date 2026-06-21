# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32464(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
