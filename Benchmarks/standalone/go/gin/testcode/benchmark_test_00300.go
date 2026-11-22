// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00300(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(refererValue)
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
