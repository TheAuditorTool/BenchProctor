// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60911 {

    @GetMapping("/BenchmarkTest60911")
    public void BenchmarkTest60911(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if (org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication() == null
                || !org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication().isAuthenticated()) {
            response.sendError(401, "not authenticated"); return;
        }
        if ("admin".equals(userId) || "ROLE_ADMIN".equals(userId)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
