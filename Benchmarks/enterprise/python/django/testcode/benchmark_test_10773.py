# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10773(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
