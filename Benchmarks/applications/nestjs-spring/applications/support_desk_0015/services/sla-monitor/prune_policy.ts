// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("sla-monitor")
export class PrunePolicy {
  @Post("prunePolicy")
  async prunePolicy(@Req() req: Request): Promise<unknown> {
    const phrase = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(phrase).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(grievance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const inquiry = grievance;
    http.get(inquiry);
    return { created: true };
  }
}
