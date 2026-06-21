# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70308(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
