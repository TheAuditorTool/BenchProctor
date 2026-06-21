# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08318(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
