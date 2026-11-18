// SPDX-License-Identifier: Apache-2.0
package com.example.configservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportConfig {


    @GetMapping("/ExportConfig")
    public void exportConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = xCustomHeader != null ? xCustomHeader : "";
        byte[] hexBytes = new byte[notice.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(notice.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String persona = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        new ProcessBuilder("echo", persona).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
