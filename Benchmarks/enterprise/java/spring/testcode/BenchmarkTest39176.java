// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest39176 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @PostMapping(path="/BenchmarkTest39176", consumes="application/xml")
    public void BenchmarkTest39176(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = expandTabs(xmlValue);
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
