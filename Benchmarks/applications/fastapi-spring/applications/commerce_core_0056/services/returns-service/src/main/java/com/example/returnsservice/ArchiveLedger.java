// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ArchiveLedger {


    @GetMapping("/ArchiveLedger")
    public void archiveLedger(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = sessionToken != null ? sessionToken : "";
        byte[] hexBytes = new byte[citation.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(citation.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String backorder = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        String voucher = backorder.matches("^(plain|markdown|html|text)$") ? backorder : "plain";
        response.getWriter().print("<div>" + voucher + "</div>");
    }
}
