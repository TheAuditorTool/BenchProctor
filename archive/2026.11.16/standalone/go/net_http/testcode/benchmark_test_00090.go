// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00090(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadedName := header.Filename
	relayPrefix := ""
	if len(uploadedName) > 0 {
		relayPrefix = strings.ToLower(uploadedName[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = uploadedName
	case "f":
		data = uploadedName
	default:
		data = uploadedName
	}
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		http.Error(w, "forbidden", http.StatusForbidden)
		return
	}
	checkedPath := "/var/app/data/" + data
	os.Remove(checkedPath)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
