// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("connector-api")
export class VerifyManifest {
  @Post("verifyManifest")
  async verifyManifest(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(caption)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const subject = caption;
    http.get(subject);
    return { created: true };
  }
}
