# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def load_summary(request):
    summary = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        subtitle = json.loads(summary).get('value', summary)
    except (json.JSONDecodeError, AttributeError):
        subtitle = summary
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", subtitle):
        return JsonResponse({'error': 'forbidden'}, status=400)
    notice = subtitle
    os.unlink('/var/app/data/' + str(notice))
    return JsonResponse({"saved": True})
