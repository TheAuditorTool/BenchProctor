// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest54837 {

    @PostMapping(path="/BenchmarkTest54837", consumes="text/plain")
    public void BenchmarkTest54837(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = String.format("%s", rawData);
        response.getWriter().print(String.valueOf(data));
    }
}
