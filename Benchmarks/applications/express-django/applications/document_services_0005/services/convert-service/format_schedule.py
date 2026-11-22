# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from pathlib import Path


@csrf_exempt
def format_schedule(request):
    footnote = request.body.decode('utf-8')
    addendum = footnote if footnote else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    dossier = addendum
    Path('/var/app/data/' + str(dossier)).write_text('data')
    return JsonResponse({"saved": True})
