# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37210(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
