// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00090(c *gin.Context) {
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
	c.Redirect(http.StatusFound, data)
}
