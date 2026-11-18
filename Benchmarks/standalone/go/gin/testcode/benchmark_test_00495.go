// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00495(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	var data string
	if len(forwardedIP) > 0 {
		data = forwardedIP
	} else {
		data = "default"
	}
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid number")
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	c.Set("data", boundedVal)
}
