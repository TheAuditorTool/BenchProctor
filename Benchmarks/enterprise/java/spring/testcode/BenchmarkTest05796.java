// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05796 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GetMapping("/BenchmarkTest05796")
    public void BenchmarkTest05796(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = toLowerCase(userId);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            response.getWriter().print("<div>" + data + "</div>");
        }
    }
}
