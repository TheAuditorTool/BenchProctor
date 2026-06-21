// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest40270 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest40270", consumes="application/xml")
    public void BenchmarkTest40270(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = normalize(xmlValue);
        String routeResult = "unknown";
        switch (data) {
            case "retry": routeResult = "retry-handled"; break;
            case "abort": routeResult = "abort-handled"; break;
        }
        response.setHeader("X-Route-Result", routeResult);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
