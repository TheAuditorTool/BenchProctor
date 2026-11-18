// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00600(c *gin.Context) {
	header, err := c.FormFile("upload")
	if err != nil {
		c.String(http.StatusBadRequest, "bad upload")
		return
	}
	uploadName := header.Filename
	var _num float64
	if _, _err := fmt.Sscanf(uploadName, "%f", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid number")
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	c.Set("data", boundedVal)
}
