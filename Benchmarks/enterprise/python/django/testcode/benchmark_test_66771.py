# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest66771(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
