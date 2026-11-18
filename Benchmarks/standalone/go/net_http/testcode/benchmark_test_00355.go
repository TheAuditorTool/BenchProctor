// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00355(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	var data string
	for _, token := range strings.Split(xmlBody, ",") {
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
