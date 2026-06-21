// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest43387 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @GET
    @Path("/BenchmarkTest43387")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest43387(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        try { AllowedValue.valueOf(uaValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { uaValue = AllowedValue.values()[0].name().toLowerCase(); }
        Object evalResult = new jakarta.el.ELProcessor().eval(uaValue);
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
