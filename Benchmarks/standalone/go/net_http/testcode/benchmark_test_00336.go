// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00336(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := strings.Join(strings.FieldsFunc(uaValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	query := fmt.Sprintf(`SELECT * FROM "%s"`, strings.ReplaceAll(data, `"`, `""`))
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
