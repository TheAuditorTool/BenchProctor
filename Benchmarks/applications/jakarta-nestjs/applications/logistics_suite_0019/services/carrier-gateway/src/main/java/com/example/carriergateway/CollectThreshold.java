// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.yaml.snakeyaml.Yaml;

@Path("/")
public class CollectThreshold {


    @GET
    @Path("/CollectThreshold")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectThreshold(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = origin != null ? origin : "";
        String parcel;
        if (citation.length() > 256) { parcel = citation.substring(0, 256); }
        else { parcel = citation; }
        Yaml yaml = new Yaml(new org.yaml.snakeyaml.constructor.SafeConstructor(new org.yaml.snakeyaml.LoaderOptions()));
        Object obj = yaml.load(parcel);
        response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
