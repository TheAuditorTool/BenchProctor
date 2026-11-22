// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00090(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	data := fmt.Sprintf("%s", authHeader)
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid integer")
		return
	}
	boundedVal := strconv.Itoa(max(0, min(_num, 2147483647)))
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
