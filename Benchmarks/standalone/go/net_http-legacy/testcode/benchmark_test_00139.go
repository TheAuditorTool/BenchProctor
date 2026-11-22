// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00139(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	fieldValue := r.FormValue("field")
	pending := strings.Split(fieldValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
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
