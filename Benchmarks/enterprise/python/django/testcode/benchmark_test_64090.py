# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64090(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    int(str(data))
    return JsonResponse({"saved": True})
