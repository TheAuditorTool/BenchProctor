// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest32506 {

    @GetMapping("/BenchmarkTest32506")
    public void BenchmarkTest32506(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : authHeader.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        if (!String.valueOf(data).equals(request.getSession().getAttribute("csrfToken"))) {
            response.sendError(403, "csrf mismatch"); return;
        }
        String sessionRole = String.valueOf(request.getSession().getAttribute("role"));
        if (!"admin".equals(sessionRole)) { response.sendError(403, "forbidden"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
