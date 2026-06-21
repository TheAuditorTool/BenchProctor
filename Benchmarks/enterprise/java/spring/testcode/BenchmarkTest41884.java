// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41884 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }
    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @GetMapping("/BenchmarkTest41884")
    public void BenchmarkTest41884(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        FormData payload = new FormData(headerValue);
        String data = payload.payload;
        synchronized(SHARED_WRITE_LOCK) {
            sharedLastValue = data;
            int seen = sharedWriteCount;
            sharedWriteCount = seen + 1;
        }
    }
}
