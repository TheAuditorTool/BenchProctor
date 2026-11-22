# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from pathlib import Path


@csrf_exempt
def publish_article(request):
    remark = request.body.decode('utf-8')
    byline = remark if remark else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(byline)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    addendum = byline
    Path('/var/app/data/' + str(addendum)).write_text('data')
    return JsonResponse({"saved": True})
