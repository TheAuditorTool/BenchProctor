// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportWindow {


    @GetMapping("/ExportWindow/{pathId}")
    public void exportWindow(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = pathId;
        String backorder = java.net.URLDecoder.decode(citation, java.nio.charset.StandardCharsets.UTF_8);
        String voucher = backorder.matches("^(plain|markdown|html|text)$") ? backorder : "plain";
        response.getWriter().print("<div>" + voucher + "</div>");
    }
}
