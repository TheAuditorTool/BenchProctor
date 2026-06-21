# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64019(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
