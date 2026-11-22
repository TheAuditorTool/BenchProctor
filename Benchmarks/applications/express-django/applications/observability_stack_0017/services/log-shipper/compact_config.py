# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re


@csrf_exempt
def compact_config(request):
    note = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    cohort = bytes.fromhex(note).decode('utf-8', 'ignore')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", cohort):
        return JsonResponse({'error': 'forbidden'}, status=400)
    gauge = cohort
    os.unlink('/var/app/data/' + str(gauge))
    return JsonResponse({"saved": True})
