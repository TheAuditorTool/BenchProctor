// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41135 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest41135/{pathId}")
    public void BenchmarkTest41135(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        holder.set(pathValue);
        String data = holder.get();
        jakarta.servlet.http.HttpSession existingSession = request.getSession(false);
        if (existingSession == null || existingSession.getAttribute("user") == null) {
            response.sendError(401, "no session"); return;
        }
        request.getSession().setAttribute("data", String.valueOf(data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
