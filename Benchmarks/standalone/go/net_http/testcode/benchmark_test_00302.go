// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00302(w http.ResponseWriter, r *http.Request) {
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
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
