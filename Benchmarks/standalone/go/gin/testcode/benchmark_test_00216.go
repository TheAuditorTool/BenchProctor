// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00216(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	relayPrefix := ""
	if len(multipartValue) > 0 {
		relayPrefix = strings.ToLower(multipartValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = multipartValue
	case "f":
		data = multipartValue
	default:
		data = multipartValue
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		c.String(http.StatusInternalServerError, ldapErr.Error())
		return
	}
	defer ldapConn.Close()
	searchReq := ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, "(uid="+processed+")", []string{"cn"}, nil)
	sr, _ := ldapConn.Search(searchReq)
	if sr != nil {
		c.Header("X-LDAP-Count", strconv.Itoa(len(sr.Entries)))
	}
	c.JSON(200, gin.H{"code": "OK"})
}
