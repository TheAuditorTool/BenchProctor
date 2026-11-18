// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("mapping-store")
export class NormalizeWindow {
  @Post("normalizeWindow")
  async normalizeWindow(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.host as string) || "";
    const handshake = `${footnote}`;
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const blurb = handshake;
    http.get(blurb);
    return { created: true };
  }
}
