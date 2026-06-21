// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66574 {

    @PostMapping(path="/BenchmarkTest66574", consumes="text/plain")
    public void BenchmarkTest66574(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = rawData.replace("\u0000", "");
        response.sendError(500, data);
    }
}
