# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05222(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
