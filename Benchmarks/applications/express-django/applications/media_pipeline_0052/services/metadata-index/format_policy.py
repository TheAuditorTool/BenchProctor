# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def format_policy(request):
    tagline = request.body.decode('utf-8')
    rendition = tagline if tagline else 'default'
    parsed = yaml.safe_load(rendition)
    return JsonResponse({'parsed': str(parsed)}, status=200)
