// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RotateSnapshot {


    @GetMapping("/RotateSnapshot")
    public void rotateSnapshot(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = sessionToken != null ? sessionToken : "";
        byte[] hexBytes = new byte[note.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(note.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String inquiry = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        String grievance = inquiry.matches("^(plain|markdown|html|text)$") ? inquiry : "plain";
        response.getWriter().print("<div>" + grievance + "</div>");
    }
}
