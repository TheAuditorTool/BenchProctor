// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67335 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GetMapping("/BenchmarkTest67335")
    public void BenchmarkTest67335(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = collapseWhitespace(originValue);
        if (org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication() == null
                || !org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication().isAuthenticated()) {
            response.sendError(401, "not authenticated"); return;
        }
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
