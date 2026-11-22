# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def summarize_summary(request):
    note = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    byline = normalize(note)
    return HttpResponse(mark_safe('<div>' + str(byline) + '</div>'))
