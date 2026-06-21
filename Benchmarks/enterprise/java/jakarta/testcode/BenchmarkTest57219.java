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
public class BenchmarkTest57219 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest57219/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest57219(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        String checkedPath = "/var/app/data/" + java.nio.file.Paths.get(data).getFileName().toString();
        String content = Files.readString(Paths.get(checkedPath), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
