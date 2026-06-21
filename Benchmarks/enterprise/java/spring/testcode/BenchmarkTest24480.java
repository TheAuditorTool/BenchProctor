// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest24480 {

    @GetMapping("/BenchmarkTest24480/{pathId}")
    public void BenchmarkTest24480(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        System.loadLibrary(pathValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
