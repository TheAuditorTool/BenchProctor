// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00160(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := string(bytes.TrimSpace([]byte(rawBody)))
	var matched []User
	if err := gormDB.Raw(fmt.Sprintf(`SELECT id, name FROM "%s"`, strings.ReplaceAll(data, `"`, `""`))).Scan(&matched).Error; err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
