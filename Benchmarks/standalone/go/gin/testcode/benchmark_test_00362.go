// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00362(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	var data string
	for _, token := range strings.Split(jsonValue, ",") {
		data = token
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	c.JSON(http.StatusOK, map[string]string{"hash": hashStr})
}
