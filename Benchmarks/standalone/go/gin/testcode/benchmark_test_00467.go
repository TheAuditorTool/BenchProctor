// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00467(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := forwardedIP
	if _, after, ok := strings.Cut(forwardedIP, ","); ok {
		data = after
	}
	c.Set("data", data)
}
