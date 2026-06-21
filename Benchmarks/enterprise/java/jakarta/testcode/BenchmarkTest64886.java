// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest64886 {

    @POST
    @Path("/BenchmarkTest64886")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest64886(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.function.Function<String, String> preprocessor = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::strip);
        String data = fullPipeline.apply(rawData);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Object evaluated = new jakarta.el.ELProcessor().eval(data);
            return Response.ok("<div>" + evaluated + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
