// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00356 {

    private enum AllowedValue { PLAIN, MARKDOWN, HTML, TEXT }

    @GET
    @Path("/BenchmarkTest00356")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00356(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + forwardedIp;
        String data = valueSupplier.get();
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
