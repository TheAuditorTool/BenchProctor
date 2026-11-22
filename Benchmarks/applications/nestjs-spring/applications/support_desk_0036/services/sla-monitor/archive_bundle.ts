// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("sla-monitor")
export class ArchiveBundle {
  @Post("archiveBundle")
  async archiveBundle(@Req() req: Request): Promise<unknown> {
    const preface = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(preface).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(grievance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const inquiry = grievance;
    http.get(inquiry);
    return { created: true };
  }
}
