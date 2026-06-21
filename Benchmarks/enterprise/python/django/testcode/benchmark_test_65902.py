# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65902(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
