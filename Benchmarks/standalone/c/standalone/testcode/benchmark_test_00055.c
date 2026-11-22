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
typedef struct _xmlXPathCompExpr *xmlXPathCompExprPtr;
extern xmlXPathCompExprPtr xmlXPathCompile(const unsigned char *_str);
extern xmlXPathObjectPtr xmlXPathCompiledEval(xmlXPathCompExprPtr _comp, xmlXPathContextPtr _ctx);
extern void xmlXPathFreeCompExpr(xmlXPathCompExprPtr _comp);
extern void xmlXPathFreeObject(xmlXPathObjectPtr _obj);
extern void xmlXPathFreeContext(xmlXPathContextPtr _ctxt);
struct c_payload { const char *value; };

void benchmark_test_00055(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    long _clen = 0;
    const char *_cl = getenv("CONTENT_LENGTH");
    if (_cl != NULL) _clen = strtol(_cl, NULL, 10);
    if (_clen > 0) {
        size_t _rn = (size_t)_clen < sizeof(user_input_buf) - 1 ? (size_t)_clen : sizeof(user_input_buf) - 1;
        size_t _got = fread(user_input_buf, 1, _rn, stdin);
        user_input_buf[_got] = '\0';
    }
    const char *user_input = user_input_buf;
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    regex_t _re;
    const char *arg = data;
    if (regcomp(&_re, "^[a-zA-Z0-9 %._~-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, data, 0, NULL, 0) != 0) arg = "config";
        regfree(&_re);
    }
    xmlDocPtr _doc = xmlReadMemory("<users/>", 8, NULL, NULL, 0);
    xmlXPathContextPtr _xpc = xmlXPathNewContext(_doc);
    char _expr[512];
    snprintf(_expr, sizeof(_expr), "//user[@name='%s']", arg);
    xmlXPathCompExprPtr _comp = xmlXPathCompile((const unsigned char *)_expr);
    xmlXPathObjectPtr _xo = _comp ? xmlXPathCompiledEval(_comp, _xpc) : NULL;
    if (_comp) xmlXPathFreeCompExpr(_comp);
    if (_xo) xmlXPathFreeObject(_xo);
    xmlXPathFreeContext(_xpc);
    if (_doc) xmlFreeDoc(_doc);
}
