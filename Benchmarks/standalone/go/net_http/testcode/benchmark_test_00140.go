// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00140(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data := strings.ReplaceAll(userID, "\x00", "")
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
