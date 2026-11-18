// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00025 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    @POST
    @Path("/BenchmarkTest00025")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00025(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.function.Supplier<String> valueSupplier = () -> rawData.strip();
        String data = valueSupplier.get();
        Object codeResult = new jakarta.el.ELProcessor().eval(data);
        response.setHeader("X-Code-Result", String.valueOf(codeResult));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
