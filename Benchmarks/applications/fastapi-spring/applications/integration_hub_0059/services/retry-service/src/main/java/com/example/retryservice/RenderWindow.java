// SPDX-License-Identifier: Apache-2.0
package com.example.retryservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderWindow {


    @GetMapping("/RenderWindow")
    public void renderWindow(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = sessionToken != null ? sessionToken : "";
        String handshake = synopsis.isEmpty() ? "default" : synopsis;
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
