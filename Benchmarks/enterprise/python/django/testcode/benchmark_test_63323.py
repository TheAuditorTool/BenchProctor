# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest63323(request):
    upload_name = request.FILES['doc'].name
    data = '{}'.format(upload_name)
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
