// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00204(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	pending := strings.Split(authHeader, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	trustedSettings.Store("partner_callback_host", data)
	c.JSON(200, gin.H{"code": "OK"})
}
