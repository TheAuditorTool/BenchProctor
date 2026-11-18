// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00007(c *gin.Context) {
	hostValue := c.Request.Host
	data := fmt.Sprintf("%s", hostValue)
	c.Set("data", data)
}
