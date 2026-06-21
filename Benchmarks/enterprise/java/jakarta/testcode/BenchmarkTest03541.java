// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03541 {

    @POST
    @Path("/BenchmarkTest03541/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03541(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> commentValue)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        response.addCookie(new Cookie("session", data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
