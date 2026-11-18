// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"os"
	"path/filepath"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00285(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	var data string
	if len(graphqlVar) > 0 {
		data = graphqlVar
	} else {
		data = "default"
	}
	baseDir := "/var/app/data"
	cleanPath := filepath.Clean(filepath.Join(baseDir, data))
	if cleanPath != baseDir && !strings.HasPrefix(cleanPath, baseDir+"/") {
		c.String(http.StatusForbidden, "access denied")
		return
	}
	checkedPath := cleanPath
	os.WriteFile(checkedPath, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
