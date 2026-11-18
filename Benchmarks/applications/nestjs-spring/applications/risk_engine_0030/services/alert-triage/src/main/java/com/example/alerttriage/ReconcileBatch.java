// SPDX-License-Identifier: Apache-2.0
package com.example.alerttriage;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@RestController
class ReconcileBatch {


    @GetMapping("/ReconcileBatch")
    public void reconcileBatch(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(System.getenv("RISK_INPUT_0030")).orElse("");
        String prefix = summary.length() > 0 ? summary.substring(0, 1).toLowerCase() : "";
        String grievance;
        switch (prefix) {
            case "h": grievance = summary.toLowerCase(); break;
            case "f": grievance = summary.toUpperCase(); break;
            default: grievance = summary.strip(); break;
        }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(grievance);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
