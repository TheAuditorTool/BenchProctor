// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00361(c *gin.Context) {
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
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
