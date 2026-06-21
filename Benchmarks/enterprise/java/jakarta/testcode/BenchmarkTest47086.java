// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest47086 {

    @GET
    @Path("/BenchmarkTest47086")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest47086(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.join(" ", hostValue.split("\\s+"));
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(data)) { return Response.status(403).build(); }
        String allowedBin = data;
        System.loadLibrary(allowedBin);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
