// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("recovery-service")
export class RenderReport {
  @Post("renderReport")
  async renderReport(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.host as string) || "";
    const persona = `${paragraph}`;
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const synopsis = persona;
    http.get(synopsis);
    return { created: true };
  }
}
