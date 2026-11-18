// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strconv"

	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00371(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	var data string
	if len(cookieValue) > 0 {
		data = cookieValue
	} else {
		data = "default"
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		http.Error(w, ldapErr.Error(), http.StatusInternalServerError)
		return
	}
	defer ldapConn.Close()
	searchReq := ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, "(uid="+processed+")", []string{"cn"}, nil)
	sr, _ := ldapConn.Search(searchReq)
	if sr != nil {
		w.Header().Set("X-LDAP-Count", strconv.Itoa(len(sr.Entries)))
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
