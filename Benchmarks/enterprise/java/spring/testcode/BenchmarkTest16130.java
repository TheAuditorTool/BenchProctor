// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16130 {

    @GetMapping("/BenchmarkTest16130")
    public void BenchmarkTest16130(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        if (org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication() == null
                || !org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication().isAuthenticated()) {
            response.sendError(401, "not authenticated"); return;
        }
        String oldSessionId = request.getSession().getId();
        request.getSession().invalidate();
        request.getSession(true).setAttribute("rotated_from", oldSessionId);
        if (request.getSession().getAttribute("user") == null) { response.sendError(401); return; }
        request.getSession().setAttribute("data", String.valueOf(envValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
