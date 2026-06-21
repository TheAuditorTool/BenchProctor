// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest26800 {

    private static String trimEnds(String v) { return v.trim(); }

    @GET
    @Path("/BenchmarkTest26800")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26800(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = trimEnds(authHeader);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            response.getWriter().print("<div>" + data + "</div>");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok().build();
    }
}
