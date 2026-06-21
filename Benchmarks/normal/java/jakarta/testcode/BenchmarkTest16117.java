// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16117 {

    @GET
    @Path("/BenchmarkTest16117")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16117(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = String.format("%s", authHeader);
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
