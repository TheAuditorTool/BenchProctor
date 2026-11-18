// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00573(c *gin.Context) {
	userID := c.Query("id")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", userID)
	data := relayBuilder.String()
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid number")
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	c.Set("data", boundedVal)
}
