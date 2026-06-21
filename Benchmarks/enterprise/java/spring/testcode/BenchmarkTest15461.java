// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest15461 {

    @PostMapping(path="/BenchmarkTest15461", consumes="multipart/form-data")
    public void BenchmarkTest15461(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        if (!uploadName.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        String normalized = java.text.Normalizer.normalize(uploadName, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        response.getWriter().print("<p>" + normalized + "</p>");
    }
}
