// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"fmt"
	"io/ioutil"
	"math/big"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00299(c *gin.Context) {
	rawBytes, err := ioutil.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	relayPrefix := ""
	if len(rawBody) > 0 {
		relayPrefix = strings.ToLower(rawBody[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = rawBody
	case "f":
		data = rawBody
	default:
		data = rawBody
	}
	otpValue, err := rand.Int(rand.Reader, big.NewInt(1000000))
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	otpCode := fmt.Sprintf("%06d", otpValue.Int64())
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	c.JSON(http.StatusOK, map[string]string{"status": "challenge_sent"})
}
