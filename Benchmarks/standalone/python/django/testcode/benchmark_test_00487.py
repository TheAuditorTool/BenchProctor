# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00487(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
