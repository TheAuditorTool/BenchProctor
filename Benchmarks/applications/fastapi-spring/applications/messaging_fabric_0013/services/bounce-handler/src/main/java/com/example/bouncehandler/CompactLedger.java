// SPDX-License-Identifier: Apache-2.0
package com.example.bouncehandler;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactLedger {


    @GetMapping("/CompactLedger")
    public void compactLedger(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = xCustomHeader != null ? xCustomHeader : "";
        byte[] hexBytes = new byte[summary.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(summary.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String bulletin = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + bulletin}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
