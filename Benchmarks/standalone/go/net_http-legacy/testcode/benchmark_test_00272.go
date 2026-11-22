// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"net/http"
)

func BenchmarkTest00272(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	_fileBytes, _ := ioutil.ReadFile("/var/app/data.txt")
	fileValue := string(_fileBytes)
	decodedBytes, _ := base64.StdEncoding.DecodeString(fileValue)
	data := string(decodedBytes)
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", data)
	rows, err := DB.Query(query)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
