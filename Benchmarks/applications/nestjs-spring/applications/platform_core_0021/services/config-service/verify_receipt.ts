// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("config-service")
export class VerifyReceipt {
  @Post("verifyReceipt")
  async verifyReceipt(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(excerpt).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const persona = handshake;
    http.get(persona);
    return { created: true };
  }
}
