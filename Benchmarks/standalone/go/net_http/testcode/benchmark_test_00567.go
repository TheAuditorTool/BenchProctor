// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00567(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data := strings.Join(strings.FieldsFunc(fieldValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
