// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest67806 {

    @GET
    @Path("/BenchmarkTest67806")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest67806(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : hostValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        return Response.status(500).entity(data).build();
    }
}
