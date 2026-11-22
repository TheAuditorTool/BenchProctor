# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re


@csrf_exempt
def reconcile_checkpoint(request):
    excerpt = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    verdict = bytes.fromhex(excerpt).decode('utf-8', 'ignore')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", verdict):
        return JsonResponse({'error': 'forbidden'}, status=400)
    grievance = verdict
    os.unlink('/var/app/data/' + str(grievance))
    return JsonResponse({"saved": True})
