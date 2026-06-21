# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07918(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
