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
struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00107(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_FORWARDED_FOR");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    std::string _xsrc = "<users><user name=\"admin\" role=\"root\"/></users>";
    xmlDocPtr _xdoc = xmlReadMemory(_xsrc.c_str(), (int)_xsrc.size(), "users.xml", nullptr, XML_PARSE_NONET);
    xmlXPathContextPtr _xctx = xmlXPathNewContext(_xdoc);
    std::string _xexpr = std::string("/users/user[@name='") + data + "']";
    xmlXPathObjectPtr _xobj = xmlXPathEvalExpression(reinterpret_cast<const unsigned char *>(_xexpr.c_str()), _xctx);
    if (_xobj) xmlXPathFreeObject(_xobj);
    xmlXPathFreeContext(_xctx);
    xmlFreeDoc(_xdoc);
}
