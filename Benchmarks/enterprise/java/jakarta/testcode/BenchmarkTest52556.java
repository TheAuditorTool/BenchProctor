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
public class BenchmarkTest52556 {

    @GET
    @Path("/BenchmarkTest52556")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest52556(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data").toRealPath();
        java.nio.file.Path resolved = base.resolve(authHeader).toRealPath();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String checkedPath = resolved.toString();
        String content = Files.readString(Paths.get(checkedPath), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
