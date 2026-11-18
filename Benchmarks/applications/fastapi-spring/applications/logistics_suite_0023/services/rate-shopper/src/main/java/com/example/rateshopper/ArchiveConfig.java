// SPDX-License-Identifier: Apache-2.0
package com.example.rateshopper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ArchiveConfig {


    @GetMapping("/ArchiveConfig")
    public void archiveConfig(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = sessionToken != null ? sessionToken : "";
        String parcel = caption.isEmpty() ? "default" : caption;
        response.getWriter().print("<div>" + parcel + "</div>");
    }
}
