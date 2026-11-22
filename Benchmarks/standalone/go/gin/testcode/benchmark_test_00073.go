// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00073(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", authHeader)
	data := relayBuilder.String()
	trustedSettings.Store("partner_callback_host", data)
	c.JSON(200, gin.H{"code": "OK"})
}
