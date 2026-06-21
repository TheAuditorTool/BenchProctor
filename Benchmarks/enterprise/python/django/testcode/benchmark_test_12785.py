# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12785(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
