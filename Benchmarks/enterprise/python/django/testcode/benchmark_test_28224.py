# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28224(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
