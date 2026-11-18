// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("platform-api")
export class NormalizeProfile {
  @Post("normalizeProfile")
  async normalizeProfile(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.body as string) || "";
    const handshake = Buffer.from(excerpt, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const persona = handshake;
    http.get(persona);
    return { created: true };
  }
}
