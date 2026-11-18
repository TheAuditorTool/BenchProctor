// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00387(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	data := fmt.Sprintf("%s", uaValue)
	c.Set("data", data)
}
