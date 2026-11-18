// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00279(c *gin.Context) {
	hostValue := c.Request.Host
	content, err := os.ReadFile("/var/app/data/" + hostValue)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
