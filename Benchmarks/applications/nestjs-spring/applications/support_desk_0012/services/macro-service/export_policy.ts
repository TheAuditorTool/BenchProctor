// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("macro-service")
export class ExportPolicy {
  @Post("exportPolicy")
  async exportPolicy(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(grievance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const inquiry = grievance;
    net.connect(80, new URL(String(inquiry)).hostname);
    return { created: true };
  }
}
