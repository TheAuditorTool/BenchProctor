// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <regex>

typedef struct ldap LDAP; typedef struct ldapmsg LDAPMessage;
extern "C" int ldap_initialize(LDAP **, const char *);
extern "C" int ldap_search_ext_s(LDAP *, const char *, int, const char *, char **, int, void *, void *, void *, int, LDAPMessage **);
extern "C" int ldap_msgfree(LDAPMessage *);
extern "C" int ldap_unbind_ext_s(LDAP *, void *, void *);
enum { LDAP_SCOPE_SUBTREE = 2 };
struct berval { unsigned long bv_len; char *bv_val; };
extern "C" int ldap_compare_ext_s(LDAP *, const char *, const char *, struct berval *, void *, void *);
enum { LDAP_COMPARE_TRUE = 6 };
struct Payload { std::string value; };

void benchmark_test_00164(int, char **)
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
    Payload _pd{user_input};
    std::string data = _pd.value;
    static const std::regex _re("^[a-zA-Z0-9 _.#%\\-]+$");
    std::string arg = std::regex_match(data, _re) ? data : std::string("default");
    LDAP *_ld = nullptr;
    const char *_ldap_url = std::getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url ? _ldap_url : "ldap://directory:1389");
    std::string _dn = std::string("uid=") + arg + ",ou=people,dc=example,dc=com";
    struct berval _role = { 5, const_cast<char *>("admin") };
    int _rc = ldap_compare_ext_s(_ld, _dn.c_str(), "employeeType", &_role, nullptr, nullptr);
    std::cout << (_rc == LDAP_COMPARE_TRUE ? "admin" : "user") << std::endl;
    ldap_unbind_ext_s(_ld, nullptr, nullptr);
}
