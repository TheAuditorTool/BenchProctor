# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest66602(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
