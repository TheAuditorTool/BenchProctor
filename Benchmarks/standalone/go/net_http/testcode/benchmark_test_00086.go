// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00086(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	data := fmt.Sprintf("%s", commentText)
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
	os.WriteFile(checkedPath, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
