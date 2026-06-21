// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest82187 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest82187/{pathId}")
    public void BenchmarkTest82187(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = stripCRLF(pathValue);
        request.isUserInRole("ADMIN");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
