// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest44975 {

    @GetMapping("/BenchmarkTest44975")
    public void BenchmarkTest44975(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(originValue);
        String data = carrier.toString();
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
