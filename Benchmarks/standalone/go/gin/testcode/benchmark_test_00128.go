// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00128(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	capture := func() string { return strings.TrimSpace(jsonValue) }
	data := capture()
	trustedSettings.Store("partner_callback_host", data)
	c.JSON(200, gin.H{"code": "OK"})
}
