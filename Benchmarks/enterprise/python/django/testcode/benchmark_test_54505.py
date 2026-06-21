# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54505(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
