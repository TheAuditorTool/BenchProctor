// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest33982 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    private static final java.util.concurrent.Semaphore RATE_LIMITER = new java.util.concurrent.Semaphore(10);

    @POST
    @Path("/BenchmarkTest33982")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest33982(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        String prefix = jsonValue.length() > 0 ? jsonValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = jsonValue.toLowerCase(); break;
            case "f": data = jsonValue.toUpperCase(); break;
            default: data = jsonValue.strip(); break;
        }
        if (!RATE_LIMITER.tryAcquire(1, java.util.concurrent.TimeUnit.SECONDS)) {
            return Response.status(429).entity("rate limited").build();
        }
        try {
            byte[] buf = new byte[Math.min(Integer.parseInt(data), 1048576)];
        } finally { RATE_LIMITER.release(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
