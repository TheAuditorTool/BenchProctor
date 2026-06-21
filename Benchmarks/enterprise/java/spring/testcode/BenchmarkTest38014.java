// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38014 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping("/BenchmarkTest38014")
    public void BenchmarkTest38014(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        atomicValue.set(fieldValue);
        String data = atomicValue.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
