// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04988 {

    private static String expandTabs(String v) { return v.replace("\t", " "); }

    @GetMapping("/BenchmarkTest04988")
    public void BenchmarkTest04988(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = expandTabs(userId);
        byte[] digest = MessageDigest.getInstance("MD5").digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
