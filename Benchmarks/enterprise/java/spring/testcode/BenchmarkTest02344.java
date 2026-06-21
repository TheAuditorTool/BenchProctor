// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02344 {

    @GetMapping("/BenchmarkTest02344")
    public void BenchmarkTest02344(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if (!userId.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        response.setHeader("X-Forwarded-For", userId);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
