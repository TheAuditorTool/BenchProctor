// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16248 {

    @GET
    @Path("/BenchmarkTest16248")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16248(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(hostValue);
        String data = envelope.toString();
        if ("admin".equals(data)) {
            return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
