// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50488 {

    @PostMapping(path="/BenchmarkTest50488", consumes="application/xml")
    public void BenchmarkTest50488(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        if (org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication() == null
                || !org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication().isAuthenticated()) {
            response.sendError(401, "not authenticated"); return;
        }
        if (request.getSession().getAttribute("user") == null) { response.sendError(401); return; }
        request.getSession().setAttribute("data", String.valueOf(xmlValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
