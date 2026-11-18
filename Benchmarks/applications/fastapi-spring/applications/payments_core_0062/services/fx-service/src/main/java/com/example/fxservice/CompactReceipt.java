// SPDX-License-Identifier: Apache-2.0
package com.example.fxservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactReceipt {


    @GetMapping("/CompactReceipt")
    public void compactReceipt(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = sessionToken != null ? sessionToken : "";
        String disbursement;
        try { disbursement = new String(java.util.Base64.getDecoder().decode(headline), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { disbursement = headline; }
        response.getWriter().print("<div>" + disbursement + "</div>");
    }
}
