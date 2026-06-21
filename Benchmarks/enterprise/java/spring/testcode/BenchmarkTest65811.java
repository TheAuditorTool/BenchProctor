// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65811 {

    @PostMapping(path="/BenchmarkTest65811", consumes="text/plain")
    public void BenchmarkTest65811(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        if (!String.valueOf(rawData).equals(request.getSession().getAttribute("csrfToken"))) {
            response.sendError(403, "csrf mismatch"); return;
        }
        String sessionRole = String.valueOf(request.getSession().getAttribute("role"));
        if (!"admin".equals(sessionRole)) { response.sendError(403, "forbidden"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
