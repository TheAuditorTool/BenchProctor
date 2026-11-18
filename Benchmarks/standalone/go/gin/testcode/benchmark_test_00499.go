// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00499(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	c.Set("data", forwardedIP)
}
