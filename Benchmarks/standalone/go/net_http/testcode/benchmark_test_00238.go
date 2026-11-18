// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
)

func BenchmarkTest00238(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var data string
	if authHeader != "" {
		data = authHeader
	}
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
