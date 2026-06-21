# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest44339(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
