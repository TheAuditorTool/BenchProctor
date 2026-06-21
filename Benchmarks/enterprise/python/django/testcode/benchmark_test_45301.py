# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45301(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
