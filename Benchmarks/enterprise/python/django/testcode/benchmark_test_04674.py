# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04674(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
