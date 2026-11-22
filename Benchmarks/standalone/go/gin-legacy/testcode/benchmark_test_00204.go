// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00204(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(authHeader)
	_lower := strings.ToLower(data)
	if !strings.HasPrefix(_lower, "t") && !strings.HasPrefix(_lower, "f") && _lower != "1" && _lower != "0" {
		c.String(http.StatusBadRequest, "invalid boolean")
		return
	}
	parsedBool := strconv.FormatBool(strings.HasPrefix(_lower, "t") || _lower == "1")
	trustedSettings.Store("partner_callback_host", parsedBool)
	c.JSON(200, gin.H{"code": "OK"})
}
