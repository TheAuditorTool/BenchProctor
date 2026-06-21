# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32523(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
