// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest14118 {

    @POST
    @Path("/BenchmarkTest14118")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14118(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + rawData;
        String data = valueSupplier.get();
        Object evaluated = new jakarta.el.ELProcessor().eval(data);
        return Response.ok("<div>" + evaluated + "</div>", MediaType.TEXT_HTML).build();
    }
}
