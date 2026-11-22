# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re


@csrf_exempt
def format_batch(request):
    summary = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    consignment = bytes.fromhex(summary).decode('utf-8', 'ignore')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", consignment):
        return JsonResponse({'error': 'forbidden'}, status=400)
    parcel = consignment
    os.unlink('/var/app/data/' + str(parcel))
    return JsonResponse({"saved": True})
