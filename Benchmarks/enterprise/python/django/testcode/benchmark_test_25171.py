# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest25171(request):
    upload_name = request.FILES['doc'].name
    data = '%s' % str(upload_name)
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
