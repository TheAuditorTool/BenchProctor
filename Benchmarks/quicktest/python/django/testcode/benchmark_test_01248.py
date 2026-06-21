# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest01248(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
