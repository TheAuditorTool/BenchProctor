// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("case-service")
export class FetchWindow {
  @Post("fetchWindow")
  async fetchWindow(@Req() req: Request): Promise<unknown> {
    const subject = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(subject).split(',')) { parts.push(token); }
    const grievance: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(grievance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const verdict = grievance;
    net.connect(80, new URL(String(verdict)).hostname);
    return { created: true };
  }
}
