// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00293(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	segments := strings.Split(uaValue, ",")
	data := strings.Join(segments, " ")
	c.Set("data", data)
}
