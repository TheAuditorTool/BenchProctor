// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68789 {

    @PostMapping(path="/BenchmarkTest68789", consumes="text/plain")
    public void BenchmarkTest68789(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(rawData, "cookie");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        String accessLevel = "none";
        switch (data) {
            case "retry": accessLevel = "scoped-primary";
            case "abort": accessLevel = accessLevel + "+escalated"; break;
            case "ignore": accessLevel = "scoped-tertiary"; break;
            default: break;
        }
        response.setHeader("X-Access-Level", accessLevel);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
