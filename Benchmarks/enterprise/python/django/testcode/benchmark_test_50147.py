# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50147(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
