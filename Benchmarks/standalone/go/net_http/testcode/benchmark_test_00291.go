// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00291(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	var data string
	if len(multipartValue) > 0 {
		data = multipartValue
	} else {
		data = "default"
	}
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	if result == nil {
		http.Error(w, "not found", 404)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"name": *result})
}
