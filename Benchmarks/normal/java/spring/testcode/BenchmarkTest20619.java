// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20619 {

    @GetMapping("/BenchmarkTest20619")
    public void BenchmarkTest20619(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        if ("admin".equals(authHeader)) {
            response.getWriter().print("{\"role\":\"admin\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
