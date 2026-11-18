// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00416(c *gin.Context) {
	hostValue := c.Request.Host
	data := strings.Join(strings.FieldsFunc(hostValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	checkedPath := "/var/app/data/" + data
	os.WriteFile(checkedPath, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
