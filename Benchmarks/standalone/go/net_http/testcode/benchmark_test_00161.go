// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"fmt"
	"net/http"
)

func BenchmarkTest00161(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	hexBytes, _ := hex.DecodeString(headerValue)
	data := string(hexBytes)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
