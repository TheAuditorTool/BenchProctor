// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00063(c *gin.Context) {
	header, err := c.FormFile("upload")
	if err != nil {
		c.String(http.StatusBadRequest, "bad upload")
		return
	}
	uploadedName := header.Filename
	relayPrefix := ""
	if len(uploadedName) > 0 {
		relayPrefix = strings.ToLower(uploadedName[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = uploadedName
	case "f":
		data = uploadedName
	default:
		data = uploadedName
	}
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	checkedPath := "/var/app/data/" + data
	os.Remove(checkedPath)
	c.JSON(200, gin.H{"code": "OK"})
}
