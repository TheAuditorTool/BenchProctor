// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RotateSnapshot {


    @GetMapping("/RotateSnapshot")
    public void rotateSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = id != null ? id : "";
        byte[] hexBytes = new byte[note.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(note.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String inquiry = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        if (!inquiry.matches("^[a-zA-Z0-9 _.%\\-]+$")) { response.sendError(400); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + inquiry}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
