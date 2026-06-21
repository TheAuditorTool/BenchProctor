# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05233(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
