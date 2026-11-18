// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("member-directory")
export class NormalizeSnapshot {
  @Post("normalizeSnapshot")
  async normalizeSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const heading: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(heading)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const passage = heading;
    net.connect(80, new URL(String(passage)).hostname);
    return { created: true };
  }
}
