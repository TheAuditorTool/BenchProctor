// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00484(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	data := strings.Join(strings.FieldsFunc(hostValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	baseDir := "/var/app/data"
	cleanPath := filepath.Clean(filepath.Join(baseDir, data))
	resolvedPath, resolveErr := filepath.EvalSymlinks(cleanPath)
	if resolveErr != nil {
		http.Error(w, "access denied", http.StatusForbidden)
		return
	}
	if resolvedPath != baseDir && !strings.HasPrefix(resolvedPath, baseDir+"/") {
		http.Error(w, "access denied", http.StatusForbidden)
		return
	}
	checkedPath := resolvedPath
	os.Remove(checkedPath)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
