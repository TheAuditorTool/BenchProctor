// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest51969 {

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest51969")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest51969(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        sharedRef.set(userId);
        String data = sharedRef.get();
        String processed = org.owasp.encoder.Encode.forHtml(data);
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + processed + "\">", MediaType.TEXT_HTML).build();
    }
}
