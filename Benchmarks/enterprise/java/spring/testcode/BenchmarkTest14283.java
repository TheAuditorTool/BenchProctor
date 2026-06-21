// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14283 {

    @GetMapping("/BenchmarkTest14283")
    public void BenchmarkTest14283(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if ("admin".equals(userId) || "ROLE_ADMIN".equals(userId)) {
            response.getWriter().print("{\"status\":\"ok\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
