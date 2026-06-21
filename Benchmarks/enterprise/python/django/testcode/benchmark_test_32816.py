# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32816(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
