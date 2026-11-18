# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach
from app_runtime import db


@csrf_exempt
def publish_receipt(request):
    phrase = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if phrase:
        inquiry = phrase
    else:
        inquiry = ''
    grievance = bleach.clean(markdown.markdown(inquiry))
    return HttpResponse(mark_safe('<div>' + str(grievance) + '</div>'))
