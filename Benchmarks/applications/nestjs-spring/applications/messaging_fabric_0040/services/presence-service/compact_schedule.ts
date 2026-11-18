// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("presence-service")
export class CompactSchedule {
  @Post("compactSchedule")
  async compactSchedule(@Req() req: Request): Promise<unknown> {
    const preface = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(preface).split(',')) { parts.push(token); }
    const bulletin: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(bulletin)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const notice = bulletin;
    net.connect(80, new URL(String(notice)).hostname);
    return { created: true };
  }
}
