# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13832(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
