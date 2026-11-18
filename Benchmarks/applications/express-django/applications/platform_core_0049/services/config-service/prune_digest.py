# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from app_runtime import db


@csrf_exempt
def prune_digest(request):
    notice = db.fetch_one('SELECT text FROM comments LIMIT 1')
    persona = notice if notice else 'default'
    return HttpResponse(mark_safe('<div>' + str(persona) + '</div>'))
