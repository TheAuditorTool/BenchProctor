// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00533(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(forwardedIP)
	c.Set("data", data)
}
