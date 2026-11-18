// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00021(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := strings.ReplaceAll(refererValue, "\x00", "")
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
