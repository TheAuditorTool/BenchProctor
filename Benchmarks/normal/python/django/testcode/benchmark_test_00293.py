# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00293(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
