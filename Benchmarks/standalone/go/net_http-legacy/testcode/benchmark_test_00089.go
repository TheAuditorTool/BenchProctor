// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"encoding/json"
	"net/http"

	"github.com/yuin/goldmark"
)

func BenchmarkTest00089(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var parsed map[string]interface{}
	json.Unmarshal([]byte(dbValue), &parsed)
	data, _ := parsed["value"].(string)
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
