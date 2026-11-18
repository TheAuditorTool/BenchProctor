// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00221(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	pending := strings.Split(headerValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
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
	content, err := os.ReadFile(checkedPath)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
