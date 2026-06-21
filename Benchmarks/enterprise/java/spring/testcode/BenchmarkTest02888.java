// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02888 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GetMapping("/BenchmarkTest02888")
    public void BenchmarkTest02888(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = expandTabs(refererValue);
        String routeResult = "unknown";
        switch (data) {
            case "retry": routeResult = "retry-handled"; break;
            case "abort": routeResult = "abort-handled"; break;
            default: routeResult = "fallback"; break;
        }
        response.setHeader("X-Route-Result", routeResult);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
