// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00217(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	var data string
	if len(graphqlVar) > 0 {
		data = graphqlVar
	} else {
		data = "default"
	}
	baseDir := "/var/app/data"
	cleanPath := filepath.Clean(filepath.Join(baseDir, data))
	if cleanPath != baseDir && !strings.HasPrefix(cleanPath, baseDir+"/") {
		http.Error(w, "access denied", http.StatusForbidden)
		return
	}
	checkedPath := cleanPath
	os.WriteFile(checkedPath, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
