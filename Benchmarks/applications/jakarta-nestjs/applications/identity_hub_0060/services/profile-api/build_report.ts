// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("profile-api")
export class BuildReport {
  @Post("buildReport")
  async buildReport(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.cookies?.session_token as string) || "";
    const persona = paragraph != null ? paragraph : '';
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const blurb = persona;
    http.get(blurb);
    return { created: true };
  }
}
