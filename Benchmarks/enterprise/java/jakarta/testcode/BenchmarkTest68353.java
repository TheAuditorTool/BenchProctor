// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest68353 {

    @GET
    @Path("/BenchmarkTest68353")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68353(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        if (!originValue.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        Object evalResult = new jakarta.el.ELProcessor().eval(originValue);
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
