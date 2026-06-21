// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest63713 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @PostMapping("/BenchmarkTest63713")
    public void BenchmarkTest63713(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = stripCRLF(commentValue);
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        response.getWriter().print(processed + ",data\n");
    }
}
