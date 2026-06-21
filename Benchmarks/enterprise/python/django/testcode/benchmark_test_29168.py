# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest29168(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
