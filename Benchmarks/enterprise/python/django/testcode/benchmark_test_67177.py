# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67177(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
