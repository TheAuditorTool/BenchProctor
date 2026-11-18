# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def compact_digest(request, path_param):
    passage = request.path.split('/')[-1]
    parts = []
    for token in str(passage).split(','):
        parts.append(token.strip())
    dossier = ','.join(parts)
    subprocess.run('echo ' + str(dossier), shell=True)
    return JsonResponse({"saved": True})
