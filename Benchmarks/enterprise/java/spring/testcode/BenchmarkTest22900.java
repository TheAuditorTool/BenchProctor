// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22900 {

    @GetMapping("/BenchmarkTest22900")
    public void BenchmarkTest22900(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        Integer.parseInt(authHeader);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
