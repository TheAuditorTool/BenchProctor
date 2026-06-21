// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest65283 {

    @GET
    @Path("/BenchmarkTest65283")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest65283(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(uaValue);
        String data = envelope.toString();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok().build();
    }
}
