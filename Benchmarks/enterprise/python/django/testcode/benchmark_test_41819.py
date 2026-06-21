# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest41819(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
