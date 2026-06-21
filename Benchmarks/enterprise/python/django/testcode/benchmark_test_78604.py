# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78604(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
