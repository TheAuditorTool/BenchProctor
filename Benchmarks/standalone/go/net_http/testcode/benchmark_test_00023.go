// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00023(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
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
