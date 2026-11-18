// SPDX-License-Identifier: Apache-2.0
package com.example.rollbackservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ExportArtifact {


    @GetMapping("/ExportArtifact/{pathId}")
    public void exportArtifact(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = pathId;
        String remark = java.net.URLDecoder.decode(wording, java.nio.charset.StandardCharsets.UTF_8);
        String phrase = remark.matches("^(plain|markdown|html|text)$") ? remark : "plain";
        response.getWriter().print("<div>" + phrase + "</div>");
    }
}
