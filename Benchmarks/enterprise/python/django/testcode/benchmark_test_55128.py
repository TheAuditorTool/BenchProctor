# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55128(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
