// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os"
)

func BenchmarkTest00062(w http.ResponseWriter, r *http.Request) {
	_cfgBytes, _ := os.ReadFile("/etc/app/config.json")
	configValue := string(_cfgBytes)
	data := fmt.Sprintf("%s", configValue)
	rows, err := DB.Query("SELECT * FROM users WHERE id = $1", data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
