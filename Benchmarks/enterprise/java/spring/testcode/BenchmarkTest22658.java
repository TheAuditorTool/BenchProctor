// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22658 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest22658/{pathId}")
    public void BenchmarkTest22658(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        if (!String.valueOf(data).equals(request.getSession().getAttribute("csrfToken"))) {
            response.sendError(403, "csrf mismatch"); return;
        }
        String sessionRole = String.valueOf(request.getSession().getAttribute("role"));
        if (!"admin".equals(sessionRole)) { response.sendError(403, "forbidden"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
