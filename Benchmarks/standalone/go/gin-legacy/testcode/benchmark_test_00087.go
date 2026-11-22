// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00087(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	capture := func() string { return strings.TrimSpace(uaValue) }
	data := capture()
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	trustedSettings.Store("partner_callback_host", processed)
	c.JSON(200, gin.H{"code": "OK"})
}
