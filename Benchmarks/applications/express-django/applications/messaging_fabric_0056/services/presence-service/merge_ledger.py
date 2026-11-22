# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from pathlib import Path


@csrf_exempt
def merge_ledger(request):
    footnote = request.body.decode('utf-8')
    bulletin = footnote if footnote else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    snippet = bulletin
    Path('/var/app/data/' + str(snippet)).write_text('data')
    return JsonResponse({"saved": True})
