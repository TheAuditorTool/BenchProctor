// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func BenchmarkTest00560(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	relayPrefix := ""
	if len(forwardedIP) > 0 {
		relayPrefix = strings.ToLower(forwardedIP[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = forwardedIP
	case "f":
		data = forwardedIP
	default:
		data = forwardedIP
	}
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
