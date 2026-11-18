// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00493(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	data := strings.Join(strings.FieldsFunc(uploadName, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	query := fmt.Sprintf("SELECT * FROM users ORDER BY %s", processed)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
