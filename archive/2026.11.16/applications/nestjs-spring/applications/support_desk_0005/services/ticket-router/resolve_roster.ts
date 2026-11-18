// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("ticket-router")
export class ResolveRoster {
  @Post("resolveRoster")
  async resolveRoster(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.host as string) || "";
    const inquiry = `${phrase}`;
    let _host = "";
    try { _host = new URL(String(inquiry)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = inquiry;
    http.get(grievance);
    return { created: true };
  }
}
