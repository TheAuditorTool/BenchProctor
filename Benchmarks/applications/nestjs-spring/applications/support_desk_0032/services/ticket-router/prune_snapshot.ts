// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("ticket-router")
export class PruneSnapshot {
  @Post("pruneSnapshot")
  async pruneSnapshot(@Req() req: Request): Promise<unknown> {
    const note = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(note).split(',')) { parts.push(token); }
    const inquiry: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(inquiry)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = inquiry;
    http.get(grievance);
    return { created: true };
  }
}
