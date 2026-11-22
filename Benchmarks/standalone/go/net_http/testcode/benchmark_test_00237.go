// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strconv"
	"strings"

	"github.com/go-ldap/ldap/v3"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00237(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data := strings.Join(strings.FieldsFunc(fieldValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.#%\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(data, "schema"); err != nil {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		http.Error(w, ldapErr.Error(), http.StatusInternalServerError)
		return
	}
	defer ldapConn.Close()
	isAdmin, cmpErr := ldapConn.Compare("uid="+processed+",ou=people,dc=example,dc=com", "employeeType", "admin")
	if cmpErr != nil {
		http.Error(w, cmpErr.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("X-Directory-Admin", strconv.FormatBool(isAdmin))
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
