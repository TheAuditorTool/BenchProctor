// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00016(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := func(v string) string { return strings.TrimSpace(v) }(forwardedIP)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
