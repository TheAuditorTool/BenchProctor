// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00044(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := strings.ReplaceAll(headerValue, "\x00", "")
	c.Set("data", data)
}
