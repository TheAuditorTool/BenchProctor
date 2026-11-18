// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
)

func BenchmarkTest00133(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	data := fmt.Sprintf("%s", multipartValue)
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
