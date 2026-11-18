// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00422(c *gin.Context) {
	hostValue := c.Request.Host
	data := strings.Join(strings.FieldsFunc(hostValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
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
	os.Remove(checkedPath)
	c.JSON(200, gin.H{"code": "OK"})
}
