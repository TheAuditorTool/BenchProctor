// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00226(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	data := fmt.Sprintf("%s", authHeader)
	c.Set("data", data)
}
