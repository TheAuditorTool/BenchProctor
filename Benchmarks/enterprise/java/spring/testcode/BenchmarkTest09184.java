// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09184 {

    @PostMapping(path="/BenchmarkTest09184", consumes="application/xml")
    public void BenchmarkTest09184(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = String.format("%s", xmlValue);
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
