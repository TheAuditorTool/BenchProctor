// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17381 {

    @GetMapping("/BenchmarkTest17381")
    public void BenchmarkTest17381(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        StringBuilder payload = new StringBuilder();
        payload.append(originValue);
        String data = payload.toString();
        response.sendError(500, data);
    }
}
