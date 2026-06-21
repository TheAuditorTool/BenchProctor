// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest05970 {

    @PostMapping(path="/BenchmarkTest05970", consumes="multipart/form-data")
    public void BenchmarkTest05970(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{uploadName});
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(data)) { response.sendError(403); return; }
        String allowedBin = data;
        System.loadLibrary(allowedBin);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
