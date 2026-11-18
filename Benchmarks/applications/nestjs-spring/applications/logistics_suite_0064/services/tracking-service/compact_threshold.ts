// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("tracking-service")
export class CompactThreshold {
  @Post("compactThreshold")
  async compactThreshold(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const parcel: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(parcel)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = parcel;
    net.connect(80, new URL(String(consignment)).hostname);
    return { created: true };
  }
}
