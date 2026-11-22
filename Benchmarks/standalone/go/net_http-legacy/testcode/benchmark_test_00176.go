// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func BenchmarkTest00176(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	_cfgBytes, _ := ioutil.ReadFile("/etc/app/config.json")
	configValue := string(_cfgBytes)
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", configValue)
	data := relayBuilder.String()
	lookupStmt, err := DB.Prepare(fmt.Sprintf(`SELECT id, name FROM "%s"`, strings.ReplaceAll(data, `"`, `""`)))
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer lookupStmt.Close()
	rows, err := lookupStmt.Query()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
