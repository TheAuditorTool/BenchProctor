// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00113(c *gin.Context) {
	hostValue := c.Request.Host
	relayPrefix := ""
	if len(hostValue) > 0 {
		relayPrefix = strings.ToLower(hostValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = hostValue
	case "f":
		data = hostValue
	default:
		data = hostValue
	}
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
