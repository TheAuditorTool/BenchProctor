# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19355(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    exec(str(data))
    return JsonResponse({"saved": True})
