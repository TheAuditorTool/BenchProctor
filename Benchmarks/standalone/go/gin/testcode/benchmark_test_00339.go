// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00339(c *gin.Context) {
	hostValue := c.Request.Host
	data := hostValue
	if _, after, ok := strings.Cut(hostValue, ","); ok {
		data = after
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
