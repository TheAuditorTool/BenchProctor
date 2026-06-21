// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73275 {

    @GetMapping("/BenchmarkTest73275")
    public void BenchmarkTest73275(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        response.sendRedirect(authHeader);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
