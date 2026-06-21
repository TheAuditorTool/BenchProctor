// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest29742 {

    @PostMapping("/BenchmarkTest29742")
    public void BenchmarkTest29742(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(fieldValue);
        String data = bundle.toString();
        jakarta.servlet.http.HttpSession existingSession = request.getSession(false);
        if (existingSession == null || existingSession.getAttribute("user") == null) {
            response.sendError(401, "no session"); return;
        }
        request.getSession().setAttribute("data", String.valueOf(data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
