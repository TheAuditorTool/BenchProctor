# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31620(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
