// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00093(c *gin.Context) {
	hostValue := c.Request.Host
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(hostValue)
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid number")
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	redisClient.HSet(context.Background(), "session:"+c.GetString("user"), map[string]interface{}{"display_name": boundedVal, "locale": "en"})
	c.JSON(200, gin.H{"code": "OK"})
}
