// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05780 {

    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @PostMapping(path="/BenchmarkTest05780", consumes="multipart/form-data")
    public void BenchmarkTest05780(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(multipartValue);
        String data = carrier.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        sharedLastValue = processed;
        int seen = sharedWriteCount;
        sharedWriteCount = seen + 1;
    }
}
