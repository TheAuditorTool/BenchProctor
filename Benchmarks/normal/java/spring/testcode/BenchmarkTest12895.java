// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12895 {

    @GetMapping("/BenchmarkTest12895")
    public void BenchmarkTest12895(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        if (org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication() == null
                || !org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication().isAuthenticated()) {
            response.sendError(401, "not authenticated"); return;
        }
        org.springframework.security.core.Authentication auth = org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || !"admin".equals(auth.getName())) {
            response.sendError(403, "forbidden"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
