// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81589 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();
    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @PostMapping("/BenchmarkTest81589")
    public void BenchmarkTest81589(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        valueRef.set(fieldValue);
        String data = valueRef.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        sharedLastValue = processed;
        int seen = sharedWriteCount;
        sharedWriteCount = seen + 1;
    }
}
