// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00070(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := strings.ReplaceAll(refererValue, "\x00", "")
	baseDir := "/var/app/data"
	cleanPath := filepath.Clean(filepath.Join(baseDir, data))
	if cleanPath != baseDir && !strings.HasPrefix(cleanPath, baseDir+"/") {
		c.String(http.StatusForbidden, "access denied")
		return
	}
	checkedPath := cleanPath
	os.WriteFile(checkedPath, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
