// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00601 {

    @GET
    @Path("/BenchmarkTest00601")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00601(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> authHeader)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        request.getSession().setAttribute("data", String.valueOf(data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
