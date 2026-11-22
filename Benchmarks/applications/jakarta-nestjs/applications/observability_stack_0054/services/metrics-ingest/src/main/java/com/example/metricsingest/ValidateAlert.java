// SPDX-License-Identifier: Apache-2.0
package com.example.metricsingest;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class ValidateAlert {


    @POST
    @Path("/ValidateAlert")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response validateAlert(@javax.validation.constraints.Size(max = 4096) @FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = field != null ? field : "";
        java.util.function.Supplier<String> valueSupplier = () -> excerpt.strip();
        String cohort = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + cohort}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
