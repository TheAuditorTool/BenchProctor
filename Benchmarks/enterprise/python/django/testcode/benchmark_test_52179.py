# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest52179(request):
    upload_name = request.FILES['doc'].name
    data = upload_name if upload_name else 'default'
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
