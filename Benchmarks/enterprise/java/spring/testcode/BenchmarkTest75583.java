// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75583 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest75583")
    public void BenchmarkTest75583(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = normalize(fieldValue);
        String accessLevel = "none";
        switch (data) {
            case "retry": accessLevel = "scoped-primary"; break;
            case "abort": accessLevel = "scoped-secondary+escalated"; break;
            case "ignore": accessLevel = "scoped-tertiary"; break;
            default: break;
        }
        response.setHeader("X-Access-Level", accessLevel);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
