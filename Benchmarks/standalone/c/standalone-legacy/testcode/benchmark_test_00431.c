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

void benchmark_test_00431(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/tmp/data", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    regex_t _re;
    const char *arg = user_input;
    if (regcomp(&_re, "^[a-zA-Z0-9 %._~-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, user_input, 0, NULL, 0) != 0) arg = "config";
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
