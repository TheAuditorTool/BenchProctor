// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishSchedule {


    @GetMapping("/PublishSchedule")
    public void publishSchedule(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = sessionToken != null ? sessionToken : "";
        byte[] hexBytes = new byte[memo.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(memo.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String voucher = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        String backorder = voucher.matches("^(plain|markdown|html|text)$") ? voucher : "plain";
        response.getWriter().print("<div>" + backorder + "</div>");
    }
}
