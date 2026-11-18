// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00193(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	var data string
	if len(originValue) > 0 {
		data = originValue
	} else {
		data = "default"
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
