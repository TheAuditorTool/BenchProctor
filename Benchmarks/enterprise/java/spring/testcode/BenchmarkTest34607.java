// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34607 {

    @PostMapping(path="/BenchmarkTest34607", consumes="text/plain")
    public void BenchmarkTest34607(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        if (!request.isUserInRole("ADMIN")) {
            response.sendError(403, "forbidden"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
