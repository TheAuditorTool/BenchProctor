# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01528(request):
    upload_name = request.FILES['upload'].name
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
