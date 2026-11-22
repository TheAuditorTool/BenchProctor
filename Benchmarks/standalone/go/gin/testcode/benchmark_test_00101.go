// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00101(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	relayPrefix := ""
	if len(jsonValue) > 0 {
		relayPrefix = strings.ToLower(jsonValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = jsonValue
	case "f":
		data = jsonValue
	default:
		data = jsonValue
	}
	redisClient.HSet(context.Background(), "session:"+c.GetString("user"), map[string]any{"display_name": data, "locale": "en"})
	c.JSON(200, gin.H{"code": "OK"})
}
