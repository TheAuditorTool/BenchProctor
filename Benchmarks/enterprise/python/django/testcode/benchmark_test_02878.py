# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02878(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
