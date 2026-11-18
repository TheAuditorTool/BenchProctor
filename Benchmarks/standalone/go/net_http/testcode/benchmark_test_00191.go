// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00191(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data := func(v string) string { return strings.TrimSpace(v) }(fieldValue)
	checkedPath := filepath.Join("/var/app/data", filepath.Base(data))
	content, err := os.ReadFile(checkedPath)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
