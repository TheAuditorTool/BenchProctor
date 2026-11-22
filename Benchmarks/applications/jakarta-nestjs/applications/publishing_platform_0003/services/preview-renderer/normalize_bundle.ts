// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("preview-renderer")
export class NormalizeBundle {
  @Post("normalizeBundle")
  async normalizeBundle(@Req() req: Request): Promise<unknown> {
    const heading = (req.cookies?.session_token as string) || "";
    const addendum = heading != null ? heading : '';
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const byline = addendum;
    http.get(byline);
    return { created: true };
  }
}
