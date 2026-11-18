// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00194(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := func(v string) string { return strings.TrimSpace(v) }(uaValue)
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
