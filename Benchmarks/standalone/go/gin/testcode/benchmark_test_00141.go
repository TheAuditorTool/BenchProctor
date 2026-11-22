// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00141(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	var data string
	if cookieValue != "" {
		data = cookieValue
	}
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	checkedPath := "/var/app/data/" + data
	content, err := os.ReadFile(checkedPath)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
