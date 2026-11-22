// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <regex>

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
typedef struct _xmlXPathCompExpr xmlXPathCompExpr; typedef xmlXPathCompExpr *xmlXPathCompExprPtr;
extern "C" xmlXPathCompExprPtr xmlXPathCompile(const unsigned char *);
extern "C" xmlXPathObjectPtr xmlXPathCompiledEval(xmlXPathCompExprPtr, xmlXPathContextPtr);
extern "C" void xmlXPathFreeCompExpr(xmlXPathCompExprPtr);
struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00210(int, char **)
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
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    static const std::regex _re("^[a-zA-Z0-9 _.%~\\-]+$");
    std::string arg = std::regex_match(data, _re) ? data : std::string("default");
    std::string _xsrc = "<users><user name=\"admin\" role=\"root\"/></users>";
    xmlDocPtr _xdoc = xmlReadMemory(_xsrc.c_str(), (int)_xsrc.size(), "users.xml", nullptr, XML_PARSE_NONET);
    xmlXPathContextPtr _xctx = xmlXPathNewContext(_xdoc);
    std::string _xexpr = std::string("/users/user[@name='") + arg + "']";
    xmlXPathCompExprPtr _xcomp = xmlXPathCompile(reinterpret_cast<const unsigned char *>(_xexpr.c_str()));
    xmlXPathObjectPtr _xobj = _xcomp ? xmlXPathCompiledEval(_xcomp, _xctx) : nullptr;
    if (_xcomp) xmlXPathFreeCompExpr(_xcomp);
    if (_xobj) xmlXPathFreeObject(_xobj);
    xmlXPathFreeContext(_xctx);
    xmlFreeDoc(_xdoc);
}
