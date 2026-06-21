// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest32303 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest32303/{pathId}")
    public void BenchmarkTest32303(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        response.sendError(500, data);
    }
}
