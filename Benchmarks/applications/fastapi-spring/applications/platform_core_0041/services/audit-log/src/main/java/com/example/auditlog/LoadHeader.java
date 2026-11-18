// SPDX-License-Identifier: Apache-2.0
package com.example.auditlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class LoadHeader {


    @GetMapping("/LoadHeader")
    public void loadHeader(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = sessionToken != null ? sessionToken : "";
        String persona = passage.isEmpty() ? "default" : passage;
        response.getWriter().print("<div>" + persona + "</div>");
    }
}
