# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import markdown
import bleach
from app_runtime import db


@csrf_exempt
def compact_record(request):
    passage = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if passage:
        remittance = passage
    else:
        remittance = ''
    disbursement = bleach.clean(markdown.markdown(remittance))
    return HttpResponse(mark_safe('<div>' + str(disbursement) + '</div>'))
