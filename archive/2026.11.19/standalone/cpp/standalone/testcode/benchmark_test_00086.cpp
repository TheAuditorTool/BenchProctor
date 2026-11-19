// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

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

void benchmark_test_00086(int, char **)
{
    const char *user_input_env = std::getenv("MULTIPART_FIELD");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    for (std::string::size_type _i = 0; _i < user_input.size(); ++_i) {
        if (user_input[_i] == '%' && _i + 2 < user_input.size()) {
            data.push_back((char)std::strtol(user_input.substr(_i + 1, 2).c_str(), nullptr, 16));
            _i += 2;
        } else { data.push_back(user_input[_i]); }
    }
    std::string _xdoc = data;
    xmlDocPtr _xd = xmlReadMemory(_xdoc.c_str(), (int)_xdoc.size(), "payload.xml", nullptr, XML_PARSE_NOENT | XML_PARSE_DTDLOAD);
    if (_xd) xmlFreeDoc(_xd);
}
