// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportHeader {


    @GetMapping("/ExportHeader/{pathId}")
    public void exportHeader(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = pathId;
        String gauge = java.net.URLDecoder.decode(note, java.nio.charset.StandardCharsets.UTF_8);
        String cohort = gauge.matches("^(plain|markdown|html|text)$") ? gauge : "plain";
        response.getWriter().print("<div>" + cohort + "</div>");
    }
}
