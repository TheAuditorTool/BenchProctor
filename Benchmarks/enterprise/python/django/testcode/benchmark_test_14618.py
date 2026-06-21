# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14618(request):
    upload_name = request.FILES['upload'].name
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
