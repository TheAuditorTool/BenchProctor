// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00216(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var data string
	if len(refererValue) > 0 {
		data = refererValue
	} else {
		data = "default"
	}
	trustedSettings.Store("partner_callback_host", data)
	c.JSON(200, gin.H{"code": "OK"})
}
