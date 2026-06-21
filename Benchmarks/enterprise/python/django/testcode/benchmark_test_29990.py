# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29990(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    eval(str(data))
    return JsonResponse({"saved": True})
