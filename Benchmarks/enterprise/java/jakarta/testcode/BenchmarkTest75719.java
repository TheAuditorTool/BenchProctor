// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest75719 {

    @GET
    @Path("/BenchmarkTest75719")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest75719(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> cookieValue)
            .thenApply(v -> v.replaceAll("[\\x00-\\x1F]", "").strip())
            .join();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            Object evaluated = new jakarta.el.ELProcessor().eval(data);
            response.getWriter().print("<div>" + evaluated + "</div>");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok().build();
    }
}
