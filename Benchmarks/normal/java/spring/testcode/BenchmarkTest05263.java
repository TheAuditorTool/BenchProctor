// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05263 {

    @GetMapping("/BenchmarkTest05263")
    public void BenchmarkTest05263(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        if (org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication() == null
                || !org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication().isAuthenticated()) {
            response.sendError(401, "not authenticated"); return;
        }
        org.springframework.security.core.Authentication auth = org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication();
        if (!"admin".equals(auth.getName())) {
            response.sendError(403, "forbidden"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
