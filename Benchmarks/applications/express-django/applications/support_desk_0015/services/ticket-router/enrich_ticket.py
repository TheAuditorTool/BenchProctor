# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re


@csrf_exempt
def enrich_ticket(request):
    phrase = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    grievance = bytes.fromhex(phrase).decode('utf-8', 'ignore')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", grievance):
        return JsonResponse({'error': 'forbidden'}, status=400)
    inquiry = grievance
    os.unlink('/var/app/data/' + str(inquiry))
    return JsonResponse({"saved": True})
