// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest08681 {

    @POST
    @Path("/BenchmarkTest08681/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest08681(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + commentValue;
        String data = valueSupplier.get();
        String processed = org.owasp.encoder.Encode.forHtml(data);
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + processed + "\">", MediaType.TEXT_HTML).build();
    }
}
