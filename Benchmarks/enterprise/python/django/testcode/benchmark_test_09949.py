# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09949(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
