// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest02236 {

    @POST
    @Path("/BenchmarkTest02236")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02236(@FormDataParam("multipart_field") String multipartField, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> multipartValue)
            .thenApply(v -> v.length() > 256 ? v.substring(0, 256).strip() : v.strip())
            .join();
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        System.setProperty("app.user.preference", data);
        response.setHeader("X-Config-Set", "app.user.preference");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
