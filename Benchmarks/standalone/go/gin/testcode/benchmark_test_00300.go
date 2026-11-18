// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00300(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := headerValue
	if _, after, ok := strings.Cut(headerValue, ","); ok {
		data = after
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
