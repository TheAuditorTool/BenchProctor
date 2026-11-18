// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@Path("/")
class EnrichRoster {


    @GET
    @Path("/EnrichRoster")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichRoster(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = userAgent != null ? userAgent : "";
        String parcel;
        try { parcel = String.valueOf(Integer.parseInt(phrase)); }
        catch (NumberFormatException e) { parcel = phrase; }
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        String deserialized = safeMapper.readValue(parcel.getBytes(java.nio.charset.StandardCharsets.UTF_8), String.class);
        return Response.ok(deserialized, MediaType.TEXT_HTML).build();
    }
}
