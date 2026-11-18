// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00242(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	form := submissionForm{payload: refererValue}
	data := form.payload
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
