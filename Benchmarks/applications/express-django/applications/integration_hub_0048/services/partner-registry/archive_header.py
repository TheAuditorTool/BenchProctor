# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from pathlib import Path


@csrf_exempt
def archive_header(request):
    citation = request.body.decode('utf-8')
    handshake = citation if citation else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    heading = handshake
    Path('/var/app/data/' + str(heading)).write_text('data')
    return JsonResponse({"saved": True})
