// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"fmt"
	"net/http"
	"os"
)

func BenchmarkTest00047(w http.ResponseWriter, r *http.Request) {
	_fileBytes, _ := os.ReadFile("/var/app/data.txt")
	fileValue := string(_fileBytes)
	hexBytes, _ := hex.DecodeString(fileValue)
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
