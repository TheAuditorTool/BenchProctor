// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io"
	"net/http"
	"strconv"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00105(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", xmlBody)
	data := relayBuilder.String()
	var _num float64
	if _, _err := fmt.Sscanf(data, "%f", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid number")
		return
	}
	boundedVal := strconv.FormatFloat(_num, 'f', -1, 64)
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		c.String(http.StatusInternalServerError, xmlErr.Error())
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+boundedVal+"']")
	c.JSON(200, gin.H{"code": "OK"})
}
