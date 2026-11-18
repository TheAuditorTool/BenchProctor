// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00299(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", graphqlVar)
	data := relayBuilder.String()
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
