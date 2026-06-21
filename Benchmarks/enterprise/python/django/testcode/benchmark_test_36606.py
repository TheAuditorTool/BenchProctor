# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest36606(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = normalise_input(auth_header)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
