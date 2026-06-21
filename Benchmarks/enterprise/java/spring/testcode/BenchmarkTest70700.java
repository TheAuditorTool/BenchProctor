// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest70700 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest70700", consumes="multipart/form-data")
    public void BenchmarkTest70700(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        stateBox.set(multipartValue);
        String data = stateBox.get();
        if (!data.isEmpty()) throw new Exception("processing error: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
