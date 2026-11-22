// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("transform-service")
export class FormatRecord {
  @Post("formatRecord")
  async formatRecord(@Req() req: Request): Promise<unknown> {
    const caption = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(caption).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const subject = handshake;
    http.get(subject);
    return { created: true };
  }
}
