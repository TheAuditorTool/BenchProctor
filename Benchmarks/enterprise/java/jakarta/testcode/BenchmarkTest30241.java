// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest30241 {

    @GET
    @Path("/BenchmarkTest30241")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest30241(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String prefix = headerValue.length() > 0 ? headerValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = headerValue.toLowerCase(); break;
            case "f": data = headerValue.toUpperCase(); break;
            default: data = headerValue.strip(); break;
        }
        if (!data.endsWith(".jpg") && !data.endsWith(".png")) { return Response.status(400).build(); }
        String entryFile = data;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
