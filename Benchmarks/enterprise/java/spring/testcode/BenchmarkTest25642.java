// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest25642 {

    @PostMapping(path="/BenchmarkTest25642", consumes="text/plain")
    public void BenchmarkTest25642(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = rawData.replace("\u0000", "");
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
