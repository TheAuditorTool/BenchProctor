// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00450(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	data := strings.Join(strings.FieldsFunc(hostValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		http.Error(w, "forbidden", http.StatusForbidden)
		return
	}
	checkedPath := "/var/app/data/" + data
	os.WriteFile(checkedPath, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
