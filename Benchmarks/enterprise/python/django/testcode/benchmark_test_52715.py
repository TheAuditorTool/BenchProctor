# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest52715(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = default_blank(multipart_value)
    processed = data[:64]
    return JsonResponse({'error': str(processed), 'stack': repr(locals())}, status=500)
