// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderTicket {


    @GetMapping("/RenderTicket")
    public void renderTicket(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = sessionToken != null ? sessionToken : "";
        String inquiry = phrase.isEmpty() ? "default" : phrase;
        response.getWriter().print("<div>" + inquiry + "</div>");
    }
}
