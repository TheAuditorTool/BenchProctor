# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def rotate_ledger(request):
    preface = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        cohort = json.loads(preface).get('value', preface)
    except (json.JSONDecodeError, AttributeError):
        cohort = preface
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", cohort):
        return JsonResponse({'error': 'forbidden'}, status=400)
    gauge = cohort
    os.unlink('/var/app/data/' + str(gauge))
    return JsonResponse({"saved": True})
