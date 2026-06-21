// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17770 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest17770")
    public void BenchmarkTest17770(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = trimEnds(authHeader);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.sendRedirect(processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
