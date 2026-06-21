// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00466 {

    @GET
    @Path("/BenchmarkTest00466")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00466(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + hostValue;
        String data = valueSupplier.get();
        Object evaluated = new jakarta.el.ELProcessor().eval(data);
        return Response.ok("<div>" + evaluated + "</div>", MediaType.TEXT_HTML).build();
    }
}
