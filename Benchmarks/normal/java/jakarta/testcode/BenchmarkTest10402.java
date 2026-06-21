// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10402 {

    @GET
    @Path("/BenchmarkTest10402")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10402(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(authHeader);
        String data = normalizer.apply(authHeader);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            jakarta.el.ELProcessor elp = new jakarta.el.ELProcessor();
            Object rendered = elp.eval(data);
            return Response.ok("<div>" + rendered + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
