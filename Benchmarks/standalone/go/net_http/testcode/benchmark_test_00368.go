// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00368(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	data := strings.ReplaceAll(forwardedIP, "\x00", "")
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
