// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00002(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	segments := strings.Split(rawBody, ",")
	data := strings.Join(segments, " ")
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
