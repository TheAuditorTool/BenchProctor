// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("token-service")
export class BuildBatch {
  @Post("buildBatch")
  async buildBatch(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(tagline)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const note = tagline;
    http.get(note);
    return { created: true };
  }
}
