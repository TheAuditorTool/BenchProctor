// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01380 {

    @GetMapping("/BenchmarkTest01380")
    public void BenchmarkTest01380(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        request.getSession().setAttribute("data", String.valueOf(authHeader));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
