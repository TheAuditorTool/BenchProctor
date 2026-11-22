// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"

	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00073(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(userID)
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		http.Error(w, ldapErr.Error(), http.StatusInternalServerError)
		return
	}
	defer ldapConn.Close()
	isAdmin, cmpErr := ldapConn.Compare("uid="+data+",ou=people,dc=example,dc=com", "employeeType", "admin")
	if cmpErr != nil {
		http.Error(w, cmpErr.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("X-Directory-Admin", strconv.FormatBool(isAdmin))
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
