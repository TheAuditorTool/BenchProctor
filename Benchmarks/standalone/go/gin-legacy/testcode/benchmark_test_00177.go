// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"encoding/hex"
	"io"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00177(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	data := strings.ReplaceAll(jsonValue, "\x00", "")
	tokenBytes := make([]byte, 16)
	_, err := io.ReadFull(rand.Reader, tokenBytes)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	apiToken := hex.EncodeToString(tokenBytes)
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	c.JSON(http.StatusOK, map[string]string{"token": apiToken})
}
