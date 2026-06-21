// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50029 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @PostMapping(path="/BenchmarkTest50029", consumes="text/plain")
    public void BenchmarkTest50029(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        FormData payload = new FormData(rawData);
        String data = payload.payload;
        response.sendError(500, data);
    }
}
