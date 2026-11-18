// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateBundle {


    @GetMapping("/ValidateBundle")
    public void validateBundle(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = sessionToken != null ? sessionToken : "";
        byte[] hexBytes = new byte[phrase.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(phrase.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String inquiry = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        String grievance = inquiry.matches("^(plain|markdown|html|text)$") ? inquiry : "plain";
        response.getWriter().print("<div>" + grievance + "</div>");
    }
}
