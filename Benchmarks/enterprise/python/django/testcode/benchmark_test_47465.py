# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47465(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
