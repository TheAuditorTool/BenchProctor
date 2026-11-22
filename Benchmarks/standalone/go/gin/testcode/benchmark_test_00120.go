// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand/v2"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00120(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	pending := strings.Split(cookieValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	tokenRNG := rand.New(rand.NewPCG(rand.Uint64(), rand.Uint64()))
	apiToken := fmt.Sprintf("%016x", tokenRNG.Uint64())
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	c.JSON(http.StatusOK, map[string]string{"token": apiToken})
}
