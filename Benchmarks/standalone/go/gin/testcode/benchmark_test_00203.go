// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"net/url"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00203(c *gin.Context) {
	userID := c.Query("id")
	data, _ := url.QueryUnescape(userID)
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid number")
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	trustedSettings.Store("partner_callback_host", boundedVal)
	c.JSON(200, gin.H{"code": "OK"})
}
