# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def merge_digest(request):
    excerpt = request.GET.get('id', '')
    dossier, _sep, _rest = str(excerpt).partition('\x00')
    parsed = yaml.safe_load(dossier)
    return JsonResponse({'parsed': str(parsed)}, status=200)
