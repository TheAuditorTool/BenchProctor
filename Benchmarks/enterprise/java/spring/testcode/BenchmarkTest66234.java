// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest66234 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @PostMapping(path="/BenchmarkTest66234", consumes="multipart/form-data")
    public void BenchmarkTest66234(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        FormData payload = new FormData(uploadName);
        String data = payload.payload;
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(data)) { response.sendError(403); return; }
        String checkedPath = "/var/app/data/" + data;
        java.util.Set<String> allowedExt = java.util.Set.of(".jpg", ".png", ".pdf");
        int dot = checkedPath.lastIndexOf('.');
        String ext = dot >= 0 ? checkedPath.substring(dot).toLowerCase() : "";
        if (!allowedExt.contains(ext)) {
            response.sendError(400, "file type not allowed"); return;
        }
        Files.write(Paths.get("/var/uploads/" + checkedPath), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
