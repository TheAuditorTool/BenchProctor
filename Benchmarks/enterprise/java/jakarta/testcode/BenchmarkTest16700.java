// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16700 {

    @GET
    @Path("/BenchmarkTest16700")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16700(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = authHeader.replace("\u0000", "");
        try {
            Integer.parseInt(data);
        } catch (Exception e) { }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
