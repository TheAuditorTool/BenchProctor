# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def BenchmarkTest03524(request):
    upload_name = request.FILES['upload'].name
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = upload_name
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
