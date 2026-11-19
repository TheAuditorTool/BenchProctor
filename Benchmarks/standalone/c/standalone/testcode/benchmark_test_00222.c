// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <regex.h>

typedef struct _xmlDoc *xmlDocPtr;
typedef struct _xmlXPathContext *xmlXPathContextPtr;
typedef struct _xmlXPathObject *xmlXPathObjectPtr;
#define XML_PARSE_NOENT 2
#define XML_PARSE_DTDVALID 16
#define XML_PARSE_NONET 2048
#define XML_PARSE_HUGE 524288
extern xmlDocPtr xmlReadMemory(const char *_buffer, int _size, const char *_url, const char *_encoding, int _options);
extern void xmlFreeDoc(xmlDocPtr _doc);
extern xmlXPathContextPtr xmlXPathNewContext(xmlDocPtr _doc);
extern xmlXPathObjectPtr xmlXPathEvalExpression(const unsigned char *_str, xmlXPathContextPtr _ctxt);

void benchmark_test_00222(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char data[512];
    switch (user_input[0]) {
        case '\0':
            data[0] = '\0';
            break;
        default:
            snprintf(data, sizeof(data), "%s", user_input);
            break;
    }
    regex_t _re;
    const char *safe = data;
    if (regcomp(&_re, "^[a-zA-Z0-9 %._~-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, data, 0, NULL, 0) != 0) safe = "config";
        regfree(&_re);
    }
    xmlDocPtr _doc = xmlReadMemory("<users/>", 8, NULL, NULL, 0);
    xmlXPathContextPtr _xpc = xmlXPathNewContext(_doc);
    char _expr[512];
    snprintf(_expr, sizeof(_expr), "//user[@name='%s']", safe);
    xmlXPathObjectPtr _xo = xmlXPathEvalExpression((const unsigned char *)_expr, _xpc);
    (void)_xo;
    if (_doc) xmlFreeDoc(_doc);
}
