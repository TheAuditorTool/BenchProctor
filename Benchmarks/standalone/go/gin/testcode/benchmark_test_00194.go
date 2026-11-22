// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand/v2"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00194(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	relayPrefix := ""
	if len(authHeader) > 0 {
		relayPrefix = strings.ToLower(authHeader[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = authHeader
	case "f":
		data = authHeader
	default:
		data = authHeader
	}
	otpValue := rand.Int32N(1000000)
	otpCode := fmt.Sprintf("%06d", otpValue)
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	c.JSON(http.StatusOK, map[string]string{"status": "challenge_sent"})
}
