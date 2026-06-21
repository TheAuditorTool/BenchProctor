// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15387 {

    @GetMapping("/BenchmarkTest15387")
    public void BenchmarkTest15387(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        if (!("true".equals(originValue) || "false".equals(originValue))) { response.sendError(400); return; }
        response.setHeader("X-Forwarded-For", originValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
