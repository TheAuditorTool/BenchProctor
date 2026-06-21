// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00270 {

    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @PostMapping(path="/BenchmarkTest00270", consumes="application/xml")
    public void BenchmarkTest00270(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        synchronized(SHARED_WRITE_LOCK) {
            sharedLastValue = xmlValue;
            int seen = sharedWriteCount;
            sharedWriteCount = seen + 1;
        }
    }
}
