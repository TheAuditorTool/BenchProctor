// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00175(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
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
		c.String(http.StatusForbidden, "access denied")
		return
	}
	if resolvedPath != baseDir && !strings.HasPrefix(resolvedPath, baseDir+"/") {
		c.String(http.StatusForbidden, "access denied")
		return
	}
	checkedPath := resolvedPath
	os.WriteFile(checkedPath, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
