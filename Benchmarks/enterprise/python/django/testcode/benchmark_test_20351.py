# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20351(request):
    upload_name = request.FILES['upload'].name
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
