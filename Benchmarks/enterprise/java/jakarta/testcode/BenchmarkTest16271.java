// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16271 {

    @GET
    @Path("/BenchmarkTest16271")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16271(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        StringBuilder payload = new StringBuilder();
        payload.append(authHeader);
        String data = payload.toString();
        if (!data.matches("^[\\w\\s.;|&$`'\\\"_/\\-{}()=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        new ProcessBuilder("python3", "-c", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
