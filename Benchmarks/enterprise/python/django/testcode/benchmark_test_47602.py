# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47602(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
