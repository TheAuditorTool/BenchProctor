# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest50785(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    os.remove(str(data))
    return JsonResponse({"saved": True})
