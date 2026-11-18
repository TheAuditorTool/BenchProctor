// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00103(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := fmt.Sprintf("%s", headerValue)
	c.Set("data", data)
}
