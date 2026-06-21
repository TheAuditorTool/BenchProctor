// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14976 {

    @PostMapping(path="/BenchmarkTest14976", consumes="application/xml")
    public void BenchmarkTest14976(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        byte[] digest = MessageDigest.getInstance("MD5").digest(xmlValue.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
