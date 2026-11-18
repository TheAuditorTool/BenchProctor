// SPDX-License-Identifier: Apache-2.0
package com.example.shareservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AnnotateDigest {


    @PostMapping("/AnnotateDigest")
    public void annotateDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : preface.split(",")) { tokens.add(token.trim()); }
        String remark = String.join(",", tokens);
        response.getWriter().print("<div>" + remark + "</div>");
    }
}
