// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00055(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(refererValue)
	c.Set("data", data)
}
