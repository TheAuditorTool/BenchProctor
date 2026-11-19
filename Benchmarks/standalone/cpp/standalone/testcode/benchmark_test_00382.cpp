// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

typedef struct ldap LDAP; typedef struct ldapmsg LDAPMessage;
extern "C" int ldap_initialize(LDAP **, const char *);
extern "C" int ldap_search_ext_s(LDAP *, const char *, int, const char *, char **, int, void *, void *, void *, int, LDAPMessage **);
extern "C" int ldap_msgfree(LDAPMessage *);
extern "C" int ldap_unbind_ext_s(LDAP *, void *, void *);
enum { LDAP_SCOPE_SUBTREE = 2 };
static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00382(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_AUTHORIZATION");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = cpp_own(user_input);
    std::string safe = std::regex_match(data, std::regex("^(admin|user|guest|service)$")) ? data : std::string("admin");
    LDAP *_ld = nullptr;
    const char *_ldap_url = std::getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url ? _ldap_url : "ldap://directory:1389");
    std::string _filter = std::string("(uid=") + safe + ")";
    LDAPMessage *_lres = nullptr;
    ldap_search_ext_s(_ld, "dc=example,dc=com", LDAP_SCOPE_SUBTREE, _filter.c_str(), nullptr, 0, nullptr, nullptr, nullptr, 0, &_lres);
    if (_lres) ldap_msgfree(_lres);
    ldap_unbind_ext_s(_ld, nullptr, nullptr);
}
