// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00207(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	relayPrefix := ""
	if len(graphqlVar) > 0 {
		relayPrefix = strings.ToLower(graphqlVar[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = graphqlVar
	case "f":
		data = graphqlVar
	default:
		data = graphqlVar
	}
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
