// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00054(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(uaValue)
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid integer")
		return
	}
	if _num < 0 {
		_num = 0
	} else if _num > 2147483647 {
		_num = 2147483647
	}
	boundedVal := strconv.Itoa(_num)
	const exportRecordSize = 512
	const maxExportRecords = 10000
	recordCount, err := strconv.ParseInt(boundedVal, 10, 64)
	if err != nil || recordCount < 1 || recordCount > maxExportRecords {
		c.String(http.StatusBadRequest, "invalid record count")
		return
	}
	exportBuf := make([]byte, 0, recordCount*exportRecordSize)
	c.Header("X-Export-Capacity", strconv.Itoa(cap(exportBuf)))
	c.JSON(200, gin.H{"code": "OK"})
}
