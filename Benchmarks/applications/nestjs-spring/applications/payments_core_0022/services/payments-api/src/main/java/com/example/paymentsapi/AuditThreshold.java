// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AuditThreshold {


    @GetMapping("/AuditThreshold")
    public void auditThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = id != null ? id : "";
        byte[] hexBytes = new byte[subject.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(subject.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String ledger = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        if (!ledger.matches("^[a-zA-Z0-9 _.%\\-]+$")) { response.sendError(400); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + ledger}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
