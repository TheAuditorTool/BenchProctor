// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PruneReport {


    @GetMapping("/PruneReport/{pathId}")
    public void pruneReport(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = pathId;
        String remittance = java.net.URLDecoder.decode(remark, java.nio.charset.StandardCharsets.UTF_8);
        String arrears = remittance.matches("^(plain|markdown|html|text)$") ? remittance : "plain";
        response.getWriter().print("<div>" + arrears + "</div>");
    }
}
