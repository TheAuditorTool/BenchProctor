// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest58000 {

    @GetMapping("/BenchmarkTest58000")
    public void BenchmarkTest58000(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        if (org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication() == null
                || !org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication().isAuthenticated()) {
            response.sendError(401, "not authenticated"); return;
        }
        if (request.getSession().getAttribute("user") == null) { response.sendError(401); return; }
        request.getSession().setAttribute("data", String.valueOf(originValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
