# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest27750(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = normalise_input(multipart_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
