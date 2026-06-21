// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest61487 {

    @GetMapping("/BenchmarkTest61487")
    public void BenchmarkTest61487(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = originValue.isEmpty() ? "default" : originValue;
        request.isUserInRole("ADMIN");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
