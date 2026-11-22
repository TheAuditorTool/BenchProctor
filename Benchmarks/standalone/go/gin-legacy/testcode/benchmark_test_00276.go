// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00276(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := strings.ReplaceAll(refererValue, "\x00", "")
	const exportRecordSize = 512
	recordCount, err := strconv.ParseInt(data, 10, 32)
	if err != nil {
		c.String(http.StatusBadRequest, "invalid record count")
		return
	}
	exportBuf := make([]byte, 0, int32(recordCount)*exportRecordSize)
	c.Header("X-Export-Capacity", strconv.Itoa(cap(exportBuf)))
	c.JSON(200, gin.H{"code": "OK"})
}
