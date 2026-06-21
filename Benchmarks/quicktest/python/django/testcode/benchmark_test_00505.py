# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00505(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
