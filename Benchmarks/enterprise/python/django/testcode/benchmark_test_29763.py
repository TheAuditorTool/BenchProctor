# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest29763(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
