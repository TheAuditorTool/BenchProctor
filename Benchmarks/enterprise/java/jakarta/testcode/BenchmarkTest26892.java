// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest26892 {

    @GET
    @Path("/BenchmarkTest26892")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26892(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.function.Function<String, String> firstStage = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(hostValue);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Object evaluated = new jakarta.el.ELProcessor().eval(data);
            return Response.ok("<div>" + evaluated + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
