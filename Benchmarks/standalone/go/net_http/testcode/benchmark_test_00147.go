// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"regexp"
	"strconv"

	"github.com/go-ldap/ldap/v3"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00147(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var parsed map[string]interface{}
	json.Unmarshal([]byte(dbValue), &parsed)
	data, _ := parsed["value"].(string)
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
