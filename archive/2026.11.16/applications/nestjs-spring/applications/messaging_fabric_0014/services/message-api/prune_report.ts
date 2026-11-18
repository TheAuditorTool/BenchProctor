// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("message-api")
export class PruneReport {
  @Post("pruneReport")
  async pruneReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.host as string) || "";
    const bulletin = `${summary}`;
    let _host = "";
    try { _host = new URL(String(bulletin)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const notice = bulletin;
    http.get(notice);
    return { created: true };
  }
}
