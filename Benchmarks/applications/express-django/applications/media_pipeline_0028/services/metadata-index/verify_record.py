# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from pathlib import Path


@csrf_exempt
def verify_record(request):
    citation = request.body.decode('utf-8')
    rendition = citation if citation else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(rendition)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    montage = rendition
    Path('/var/app/data/' + str(montage)).write_text('data')
    return JsonResponse({"saved": True})
