// SPDX-License-Identifier: Apache-2.0
package com.example.alertrouter;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RotateCheckpoint {


    @GetMapping("/RotateCheckpoint")
    public void rotateCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = id != null ? id : "";
        byte[] hexBytes = new byte[excerpt.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(excerpt.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String gauge = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        if (!gauge.matches("^[a-zA-Z0-9 _.%\\-]+$")) { response.sendError(400); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + gauge}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
