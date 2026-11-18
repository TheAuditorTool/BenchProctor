// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00134(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	form := submissionForm{payload: fieldValue}
	data := form.payload
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
