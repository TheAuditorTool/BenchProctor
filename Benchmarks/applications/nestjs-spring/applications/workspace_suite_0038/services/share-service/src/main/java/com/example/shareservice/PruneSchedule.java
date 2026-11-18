// SPDX-License-Identifier: Apache-2.0
package com.example.shareservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PruneSchedule {


    @GetMapping("/PruneSchedule")
    public void pruneSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = id != null ? id : "";
        byte[] hexBytes = new byte[preface.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(preface.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String remark = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        if (!remark.matches("^[a-zA-Z0-9 _.%\\-]+$")) { response.sendError(400); return; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + remark}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
