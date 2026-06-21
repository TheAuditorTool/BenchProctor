// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08779 {

    private static String stripWhitespace(String v) { return v.strip(); }
    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @GetMapping("/BenchmarkTest08779")
    public void BenchmarkTest08779(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = stripWhitespace(envValue);
        sharedLastValue = data;
        int seen = sharedWriteCount;
        sharedWriteCount = seen + 1;
    }
}
