// SPDX-License-Identifier: Apache-2.0
package com.example.sessionstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderLedger {


    @GetMapping("/RenderLedger")
    public void renderLedger(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = id != null ? id : "";
        byte[] hexBytes = new byte[paragraph.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(paragraph.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String persona = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        if (!persona.matches("^[a-zA-Z0-9 _.%\\-]+$")) { response.sendError(400); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + persona}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
