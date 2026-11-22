// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00025(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var data string
	for _, token := range strings.Split(authHeader, ",") {
		data = token
	}
	checkedPath := filepath.Join("/var/app/data", filepath.Base(data))
	content, err := os.ReadFile(checkedPath)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
