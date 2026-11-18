// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00198(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", uaValue)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	RespondJSON(w, http.StatusOK, map[string]string{"name": *result})
}
