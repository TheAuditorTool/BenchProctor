// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12068 {

    @GetMapping("/BenchmarkTest12068")
    public void BenchmarkTest12068(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        byte[] buf = new byte[Integer.parseInt(authHeader)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
