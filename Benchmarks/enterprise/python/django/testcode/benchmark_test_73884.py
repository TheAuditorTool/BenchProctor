# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest73884(request):
    upload_name = request.FILES['upload'].name
    data = normalise_input(upload_name)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
