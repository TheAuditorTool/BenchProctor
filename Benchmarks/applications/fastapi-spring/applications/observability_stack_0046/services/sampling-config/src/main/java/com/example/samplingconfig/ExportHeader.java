// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ExportHeader {


    @PostMapping(path="/ExportHeader", consumes="text/plain")
    public void exportHeader(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = rawBody != null ? rawBody : "";
        byte[] raw = paragraph.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String gauge = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        String cohort = gauge.matches("^(plain|markdown|html|text)$") ? gauge : "plain";
        response.getWriter().print("<div>" + cohort + "</div>");
    }
}
