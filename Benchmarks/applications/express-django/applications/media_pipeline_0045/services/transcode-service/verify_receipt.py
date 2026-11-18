# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def verify_receipt(request):
    notice = request.META.get('HTTP_AUTHORIZATION', '')
    if notice:
        rendition = notice
    else:
        rendition = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': rendition})))
