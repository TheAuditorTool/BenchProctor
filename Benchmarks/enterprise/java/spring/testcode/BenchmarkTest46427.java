// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest46427 {

    @PostMapping(path="/BenchmarkTest46427", consumes="application/xml")
    public void BenchmarkTest46427(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String accessLevel = "none";
        switch (xmlValue) {
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
