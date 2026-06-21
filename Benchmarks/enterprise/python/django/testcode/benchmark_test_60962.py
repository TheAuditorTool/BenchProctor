# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest60962(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
