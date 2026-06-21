// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09559 {

    @PostMapping("/BenchmarkTest09559")
    public void BenchmarkTest09559(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = "" + commentValue;
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
