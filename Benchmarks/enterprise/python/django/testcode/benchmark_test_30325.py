# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest30325(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
