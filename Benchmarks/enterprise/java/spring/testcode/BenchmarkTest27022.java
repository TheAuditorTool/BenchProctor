// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest27022 {

    @PostMapping(path="/BenchmarkTest27022", consumes="multipart/form-data")
    public void BenchmarkTest27022(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(uploadName)); }
        catch (NumberFormatException e) { data = uploadName; }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data").toRealPath();
        java.nio.file.Path resolved = base.resolve(data).toRealPath();
        if (!resolved.startsWith(base)) { response.sendError(403); return; }
        String checkedPath = resolved.toString();
        String content = Files.readString(Paths.get(checkedPath), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
