# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest39734(request):
    upload_name = request.FILES['doc'].name
    os.unlink('/var/app/data/' + str(upload_name))
    return JsonResponse({"saved": True})
