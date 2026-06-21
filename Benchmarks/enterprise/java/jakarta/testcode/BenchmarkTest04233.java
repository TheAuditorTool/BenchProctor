// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04233 {

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();
    private enum AllowedValue { PLAIN, MARKDOWN, HTML, TEXT }

    @GET
    @Path("/BenchmarkTest04233")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04233(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        sharedRef.set(userId);
        String data = sharedRef.get();
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
