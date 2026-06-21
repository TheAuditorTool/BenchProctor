// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest05605 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest05605/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05605(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = stripWhitespace(pathValue);
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(data)) { return Response.status(403).build(); }
        String allowedBin = data;
        System.loadLibrary(allowedBin);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
