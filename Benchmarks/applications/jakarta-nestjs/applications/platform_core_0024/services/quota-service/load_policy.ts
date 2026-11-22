// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("quota-service")
export class LoadPolicy {
  @Post("loadPolicy")
  async loadPolicy(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(heading)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const persona = heading;
    http.get(persona);
    return { created: true };
  }
}
