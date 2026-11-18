// SPDX-License-Identifier: Apache-2.0
package com.example.changelogbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PruneIndex {


    @GetMapping("/PruneIndex")
    public void pruneIndex(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = authorization != null ? authorization : "";
        String wording;
        try { wording = new String(java.util.Base64.getDecoder().decode(footnote), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { wording = footnote; }
        response.getWriter().print("<div>" + wording + "</div>");
    }
}
