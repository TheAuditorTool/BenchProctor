// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"path/filepath"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00378(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	relayPrefix := ""
	if len(originValue) > 0 {
		relayPrefix = strings.ToLower(originValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = originValue
	case "f":
		data = originValue
	default:
		data = originValue
	}
	checkedPath := filepath.Join("/var/app/data", filepath.Base(data))
	content, err := os.ReadFile(checkedPath)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
