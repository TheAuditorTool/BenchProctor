// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03710 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GetMapping("/BenchmarkTest03710")
    public void BenchmarkTest03710(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = expandTabs(refererValue);
        if (!new java.io.File("/var/app/data", new java.io.File(data).getName()).delete()) { response.sendError(500, "delete failed"); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
