// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00081(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
	c.Set("data", data)
}
