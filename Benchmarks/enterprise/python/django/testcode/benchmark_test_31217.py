# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest31217(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
