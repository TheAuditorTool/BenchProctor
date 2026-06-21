// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00454 {

    @GetMapping("/BenchmarkTest00454")
    public void BenchmarkTest00454(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
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
