// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest48902 {

    @GetMapping("/BenchmarkTest48902")
    public void BenchmarkTest48902(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        System.loadLibrary(originValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
