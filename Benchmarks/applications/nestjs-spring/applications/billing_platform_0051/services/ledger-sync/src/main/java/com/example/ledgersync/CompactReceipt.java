// SPDX-License-Identifier: Apache-2.0
package com.example.ledgersync;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactReceipt {


    @GetMapping("/CompactReceipt")
    public void compactReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = id != null ? id : "";
        byte[] hexBytes = new byte[synopsis.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(synopsis.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String arrears = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        if (!arrears.matches("^[a-zA-Z0-9 _.%\\-]+$")) { response.sendError(400); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + arrears}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
