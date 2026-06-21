# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24305(request):
    upload_name = request.FILES['upload'].name
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
