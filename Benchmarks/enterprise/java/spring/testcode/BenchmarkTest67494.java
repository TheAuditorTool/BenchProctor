// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67494 {

    private static String sharedLastValue = "";
    private static int sharedWriteCount = 0;
    private static final Object SHARED_WRITE_LOCK = new Object();

    @PostMapping(path="/BenchmarkTest67494", consumes="application/xml")
    public void BenchmarkTest67494(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data;
        try { data = String.valueOf(Integer.parseInt(xmlValue)); }
        catch (NumberFormatException e) { data = xmlValue; }
        synchronized(SHARED_WRITE_LOCK) {
            sharedLastValue = data;
            int seen = sharedWriteCount;
            sharedWriteCount = seen + 1;
        }
    }
}
