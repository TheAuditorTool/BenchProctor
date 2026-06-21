# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00001(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
