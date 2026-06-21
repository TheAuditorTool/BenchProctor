// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest56723 {

    @PostMapping(path="/BenchmarkTest56723", consumes="text/plain")
    public void BenchmarkTest56723(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = rawData.replace("\u0000", "");
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
