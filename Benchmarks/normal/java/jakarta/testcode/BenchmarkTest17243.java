// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest17243 {

    @GET
    @Path("/BenchmarkTest17243")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest17243(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = String.format("payload=%s", authHeader);
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
