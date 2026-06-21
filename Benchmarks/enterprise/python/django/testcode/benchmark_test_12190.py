# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest12190(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
