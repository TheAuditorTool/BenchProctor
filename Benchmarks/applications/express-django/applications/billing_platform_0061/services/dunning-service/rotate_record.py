# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re


@csrf_exempt
def rotate_record(request):
    footnote = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    remittance = bytes.fromhex(footnote).decode('utf-8', 'ignore')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", remittance):
        return JsonResponse({'error': 'forbidden'}, status=400)
    arrears = remittance
    os.unlink('/var/app/data/' + str(arrears))
    return JsonResponse({"saved": True})
