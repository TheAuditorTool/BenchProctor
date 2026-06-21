# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61703(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
