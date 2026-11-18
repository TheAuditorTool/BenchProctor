// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00004(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	var data string
	for _, token := range strings.Split(multipartValue, ",") {
		data = token
	}
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	RespondJSON(w, http.StatusOK, map[string]string{"name": *result})
}
