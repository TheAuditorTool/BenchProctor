// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("alert-router")
export class RouteAlert {
  @Post("routeAlert")
  async routeAlert(@Req() req: Request): Promise<unknown> {
    const snippet = req.body.telemetry_payload || "";
    http.get(snippet);
    return { created: true };
  }
}
