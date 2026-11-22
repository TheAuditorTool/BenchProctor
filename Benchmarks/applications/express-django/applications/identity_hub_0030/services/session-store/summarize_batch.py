# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from pathlib import Path


@csrf_exempt
def summarize_batch(request):
    tagline = request.body.decode('utf-8')
    persona = tagline if tagline else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    note = persona
    Path('/var/app/data/' + str(note)).write_text('data')
    return JsonResponse({"saved": True})
