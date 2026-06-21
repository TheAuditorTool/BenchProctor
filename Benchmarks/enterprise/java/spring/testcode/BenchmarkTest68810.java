// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68810 {

    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @GetMapping("/BenchmarkTest68810")
    public void BenchmarkTest68810(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(userId, "form");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        sharedLastValue = data;
        int seen = sharedWriteCount;
        sharedWriteCount = seen + 1;
    }
}
