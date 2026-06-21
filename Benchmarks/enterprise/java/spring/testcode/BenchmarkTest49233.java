// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49233 {

    @PostMapping(path="/BenchmarkTest49233", consumes="multipart/form-data")
    public void BenchmarkTest49233(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        if (!multipartValue.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        new ProcessBuilder("python3", "-c", multipartValue).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
