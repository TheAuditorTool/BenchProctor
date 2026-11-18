// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00267(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	checkedPath := "/var/app/data/" + data
	os.Remove(checkedPath)
	c.JSON(200, gin.H{"code": "OK"})
}
