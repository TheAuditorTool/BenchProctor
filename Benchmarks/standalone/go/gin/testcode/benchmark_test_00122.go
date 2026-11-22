// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00122(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	data := jsonValue
	if _, after, ok := strings.Cut(jsonValue, ","); ok {
		data = after
	}
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		c.String(http.StatusInternalServerError, ldapErr.Error())
		return
	}
	defer ldapConn.Close()
	directoryFilter := "(&(objectClass=inetOrgPerson)(mail=" + data + "))"
	pagedResult, searchErr := ldapConn.SearchWithPaging(ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, directoryFilter, []string{"cn", "mail"}, nil), 50)
	if searchErr != nil {
		c.String(http.StatusInternalServerError, searchErr.Error())
		return
	}
	c.Header("X-Directory-Matches", strconv.Itoa(len(pagedResult.Entries)))
	c.JSON(200, gin.H{"code": "OK"})
}
