// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest55002 {

    @GET
    @Path("/BenchmarkTest55002")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest55002(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.function.Function<String, String> firstStage = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(refererValue);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Object evaluated = new jakarta.el.ELProcessor().eval(data);
            return Response.ok("<div>" + evaluated + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
