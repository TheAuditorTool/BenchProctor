// SPDX-License-Identifier: Apache-2.0
package com.example.rateshopper;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichCarrier {


    @GetMapping("/EnrichCarrier")
    public void enrichCarrier(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = xCustomHeader != null ? xCustomHeader : "";
        byte[] hexBytes = new byte[caption.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(caption.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String parcel = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        new ProcessBuilder("echo", parcel).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
