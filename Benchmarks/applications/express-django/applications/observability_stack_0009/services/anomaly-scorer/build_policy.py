# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from app_runtime import db


@csrf_exempt
def build_policy(request):
    summary = db.fetch_one('SELECT text FROM comments LIMIT 1')
    gauge = summary if summary else 'default'
    return HttpResponse(mark_safe('<div>' + str(gauge) + '</div>'))
