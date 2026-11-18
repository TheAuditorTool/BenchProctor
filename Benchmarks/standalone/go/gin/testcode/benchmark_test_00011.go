// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"os"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00011(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	os.Remove("/var/app/data/" + forwardedIP)
	c.JSON(200, gin.H{"code": "OK"})
}
