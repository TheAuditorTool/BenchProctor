// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>

typedef struct _xmlDoc xmlDoc; typedef xmlDoc *xmlDocPtr;
typedef struct _xmlXPathContext xmlXPathContext; typedef xmlXPathContext *xmlXPathContextPtr;
typedef struct _xmlXPathObject xmlXPathObject; typedef xmlXPathObject *xmlXPathObjectPtr;
extern "C" xmlDocPtr xmlReadMemory(const char *, int, const char *, const char *, int);
extern "C" void xmlFreeDoc(xmlDocPtr);
extern "C" xmlXPathContextPtr xmlXPathNewContext(xmlDocPtr);
extern "C" xmlXPathObjectPtr xmlXPathEvalExpression(const unsigned char *, xmlXPathContextPtr);
extern "C" void xmlXPathFreeObject(xmlXPathObjectPtr);
extern "C" void xmlXPathFreeContext(xmlXPathContextPtr);
enum { XML_PARSE_NOENT = 2, XML_PARSE_DTDLOAD = 4, XML_PARSE_DTDVALID = 16, XML_PARSE_NONET = 2048, XML_PARSE_HUGE = 524288 };
typedef struct _xmlParserCtxt xmlParserCtxt; typedef xmlParserCtxt *xmlParserCtxtPtr;
extern "C" xmlParserCtxtPtr xmlNewParserCtxt(void);
extern "C" xmlDocPtr xmlCtxtReadMemory(xmlParserCtxtPtr, const char *, int, const char *, const char *, int);
extern "C" void xmlFreeParserCtxt(xmlParserCtxtPtr);

void benchmark_test_00063(int, char **)
{
    std::string user_input;
    if (const char *user_input_cl = std::getenv("CONTENT_LENGTH")) {
        long user_input_n = std::strtol(user_input_cl, nullptr, 10);
        if (user_input_n > 0 && user_input_n < 1048576) {
            user_input.resize((size_t)user_input_n);
            std::cin.read(&user_input[0], user_input_n);
            user_input.resize((size_t)std::cin.gcount());
        }
    }
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string _xdoc = data;
    xmlParserCtxtPtr _xpc = xmlNewParserCtxt();
    xmlDocPtr _xd = xmlCtxtReadMemory(_xpc, _xdoc.c_str(), (int)_xdoc.size(), "payload.xml", nullptr, XML_PARSE_NOENT | XML_PARSE_DTDLOAD);
    if (_xd) xmlFreeDoc(_xd);
    xmlFreeParserCtxt(_xpc);
}
