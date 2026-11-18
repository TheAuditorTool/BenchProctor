// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00052(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(refererValue)
	c.Set("data", data)
}
