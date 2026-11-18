// SPDX-License-Identifier: Apache-2.0
package com.example.allocationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PruneAllocation {


    @GetMapping("/PruneAllocation")
    public void pruneAllocation(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = sessionToken != null ? sessionToken : "";
        byte[] hexBytes = new byte[summary.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(summary.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String restock = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        String backorder = restock.matches("^(plain|markdown|html|text)$") ? restock : "plain";
        response.getWriter().print("<div>" + backorder + "</div>");
    }
}
