# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24741(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    return JsonResponse({'error': str(forwarded_ip), 'stack': repr(locals())}, status=500)
