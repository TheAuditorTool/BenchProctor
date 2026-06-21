# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08393(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
