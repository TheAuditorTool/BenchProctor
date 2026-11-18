# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def load_threshold(request):
    passage = request.body.decode('utf-8')
    montage = passage if passage else 'default'
    rendition = bleach.clean(montage)
    return HttpResponse(mark_safe('<div>' + str(rendition) + '</div>'))
