# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest36306(request):
    upload_name = request.FILES['upload'].name
    logging.info('User action: ' + str(upload_name))
    return JsonResponse({"saved": True})
