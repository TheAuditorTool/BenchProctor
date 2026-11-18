// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00022(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := func(v string) string { return strings.TrimSpace(v) }(graphqlVar)
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	checkedPath := "/var/app/data/" + data
	os.WriteFile(checkedPath, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
