# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def summarize_record(request):
    passage = os.environ.get('DOCUMENTS_INPUT_0019', '')
    dossier = passage if passage else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(dossier)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    addendum = dossier
    subprocess.run('echo ' + str(addendum), shell=True)
    return JsonResponse({"saved": True})
