// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00270(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	var data string
	if uaValue != "" {
		data = uaValue
	}
	c.Set("data", data)
}
