// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34266 {

    @PostMapping(path="/BenchmarkTest34266", consumes="text/plain")
    public void BenchmarkTest34266(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        StringBuilder payload = new StringBuilder();
        payload.append(rawData);
        String data = payload.toString();
        response.getWriter().print(String.valueOf(data));
    }
}
