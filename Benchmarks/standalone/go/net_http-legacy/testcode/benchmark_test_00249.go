// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
)

func BenchmarkTest00249(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	refererValue := r.Header.Get("Referer")
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[refererValue] {
		http.Error(w, "forbidden", http.StatusForbidden)
		return
	}
	checkedPath := "/var/app/data/" + refererValue
	content, err := ioutil.ReadFile(checkedPath)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
