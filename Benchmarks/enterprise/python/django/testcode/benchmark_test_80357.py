# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80357(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
