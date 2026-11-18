// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00498(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := func(v string) string { return strings.TrimSpace(v) }(graphqlVar)
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		http.Error(w, "forbidden", http.StatusForbidden)
		return
	}
	checkedPath := "/var/app/data/" + data
	os.WriteFile(checkedPath, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
