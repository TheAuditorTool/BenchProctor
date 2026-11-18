// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00507(c *gin.Context) {
	userID := c.Query("id")
	relayPrefix := ""
	if len(userID) > 0 {
		relayPrefix = strings.ToLower(userID[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = userID
	case "f":
		data = userID
	default:
		data = userID
	}
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid integer")
		return
	}
	boundedVal := strconv.Itoa(max(0, min(_num, 2147483647)))
	requested, _ := strconv.Atoi(boundedVal)
	allocated := requested + 1
	c.Header("X-Alloc-Size", strconv.Itoa(allocated))
}
