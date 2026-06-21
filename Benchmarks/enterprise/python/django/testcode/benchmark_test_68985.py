# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68985(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
