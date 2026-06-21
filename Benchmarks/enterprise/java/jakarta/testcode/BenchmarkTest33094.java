// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest33094 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/BenchmarkTest33094")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest33094(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        String prefix = jsonValue.length() > 0 ? jsonValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = jsonValue.toLowerCase(); break;
            case "f": data = jsonValue.toUpperCase(); break;
            default: data = jsonValue.strip(); break;
        }
        int boundedVal;
        try { boundedVal = Integer.parseInt(data); }
        catch (NumberFormatException e) { return Response.status(400).build(); }
        if (boundedVal < 0 || boundedVal > 1048576) { return Response.status(400).build(); }
        long requested = boundedVal;
        long allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
