// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00057(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var data string
	if authHeader != "" {
		data = authHeader
	}
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
