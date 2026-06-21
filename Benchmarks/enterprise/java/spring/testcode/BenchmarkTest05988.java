// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05988 {

    @PostMapping(path="/BenchmarkTest05988", consumes="text/plain")
    public void BenchmarkTest05988(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = rawData.isEmpty() ? "default" : rawData;
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
