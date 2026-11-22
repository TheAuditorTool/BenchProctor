// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00086(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	headerValue := r.Header.Get("X-Custom-Header")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(headerValue)
	lookupStmt, err := DB.Prepare("SELECT id, name FROM users WHERE name = '" + data + "'")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer lookupStmt.Close()
	rows, err := lookupStmt.Query()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
