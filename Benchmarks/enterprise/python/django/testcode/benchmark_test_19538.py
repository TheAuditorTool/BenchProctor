# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19538(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
