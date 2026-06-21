// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest02899 {

    @GET
    @Path("/BenchmarkTest02899")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02899(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = java.net.URLDecoder.decode(userId, "UTF-8");
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(data)) { return Response.status(403).build(); }
        String allowedBin = data;
        System.loadLibrary(allowedBin);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
