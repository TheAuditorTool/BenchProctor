// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class PublishPolicy {


    @PostMapping(path="/PublishPolicy", consumes="text/plain")
    public void publishPolicy(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = rawBody != null ? rawBody : "";
        byte[] raw = footnote.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String remittance = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        String disbursement = remittance.matches("^(plain|markdown|html|text)$") ? remittance : "plain";
        response.getWriter().print("<div>" + disbursement + "</div>");
    }
}
