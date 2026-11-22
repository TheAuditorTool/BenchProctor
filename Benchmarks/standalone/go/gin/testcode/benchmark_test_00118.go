// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00118(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	content, err := os.ReadFile("/var/app/data/" + authHeader)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
