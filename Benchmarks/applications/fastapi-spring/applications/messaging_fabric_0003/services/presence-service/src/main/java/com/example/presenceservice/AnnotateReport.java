// SPDX-License-Identifier: Apache-2.0
package com.example.presenceservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AnnotateReport {


    @GetMapping("/AnnotateReport")
    public void annotateReport(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = sessionToken != null ? sessionToken : "";
        String bulletin = subject.isEmpty() ? "default" : subject;
        response.getWriter().print("<div>" + bulletin + "</div>");
    }
}
