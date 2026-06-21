// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest27425 {

    @GetMapping("/BenchmarkTest27425")
    public void BenchmarkTest27425(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(authHeader);
        String data = carrier.toString();
        response.sendError(500, data);
    }
}
