// SPDX-License-Identifier: Apache-2.0
package com.example.indexbuilder;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class SummarizeReceipt {


    @GetMapping("/SummarizeReceipt")
    public void summarizeReceipt(@javax.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = id != null ? id : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(citation, "form");
        String dossier = pair.getKey();
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + dossier + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
