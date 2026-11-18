// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00005(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	capture := func() string { return strings.TrimSpace(authHeader) }
	data := capture()
	query := fmt.Sprintf(`SELECT * FROM "%s"`, strings.ReplaceAll(data, `"`, `""`))
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
