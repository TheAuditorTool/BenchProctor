# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest68539(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
