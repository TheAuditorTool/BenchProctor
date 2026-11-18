// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00044(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", authHeader)
	data := relayBuilder.String()
	os.Remove("/var/app/data/" + data)
	c.JSON(200, gin.H{"code": "OK"})
}
