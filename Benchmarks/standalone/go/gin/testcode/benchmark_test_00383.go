// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00383(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data := func(v string) string { return strings.TrimSpace(v) }(fieldValue)
	checkedPath := filepath.Join("/var/app/data", filepath.Base(data))
	content, err := os.ReadFile(checkedPath)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
