// SPDX-License-Identifier: Apache-2.0
package com.example.configservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ValidateHeader {


    @GetMapping("/ValidateHeader")
    public void validateHeader(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = sessionToken != null ? sessionToken : "";
        byte[] hexBytes = new byte[notice.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(notice.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String persona = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        String handshake = persona.matches("^(plain|markdown|html|text)$") ? persona : "plain";
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
