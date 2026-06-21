# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40856(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '{}'.format(multipart_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
