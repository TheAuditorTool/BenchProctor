// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12329 {

    @GetMapping("/BenchmarkTest12329")
    public void BenchmarkTest12329(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = String.format("%s", originValue);
        byte[] buf = new byte[Integer.parseInt(data)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
