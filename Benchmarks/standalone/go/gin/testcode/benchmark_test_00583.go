// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00583(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(headerValue)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
