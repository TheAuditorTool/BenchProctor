// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class VerifyProfile {


    @GetMapping("/VerifyProfile")
    public void verifyProfile(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String synopsis = java.util.Optional.ofNullable(System.getenv("RISK_INPUT_0008")).orElse("");
        String prefix = synopsis.length() > 0 ? synopsis.substring(0, 1).toLowerCase() : "";
        String verdict;
        switch (prefix) {
            case "h": verdict = synopsis.toLowerCase(); break;
            case "f": verdict = synopsis.toUpperCase(); break;
            default: verdict = synopsis.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(verdict);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
