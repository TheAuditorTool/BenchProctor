// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00133(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	pending := strings.Split(uaValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
