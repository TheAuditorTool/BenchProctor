// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38750 {

    @GetMapping("/BenchmarkTest38750")
    public void BenchmarkTest38750(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        System.loadLibrary(refererValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
