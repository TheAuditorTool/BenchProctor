// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00035(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	data := strings.Join(strings.FieldsFunc(multipartValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	RespondJSON(w, http.StatusOK, map[string]string{"name": *result})
}
