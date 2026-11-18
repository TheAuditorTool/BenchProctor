// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00252(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := func(v string) string { return strings.TrimSpace(v) }(headerValue)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
