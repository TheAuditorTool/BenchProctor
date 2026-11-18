// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00019(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	data := hostValue
	if _, after, ok := strings.Cut(hostValue, ","); ok {
		data = after
	}
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	RespondJSON(w, http.StatusOK, map[string]string{"name": *result})
}
