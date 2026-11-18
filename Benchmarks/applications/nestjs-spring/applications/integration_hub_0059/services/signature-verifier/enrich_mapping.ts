// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("signature-verifier")
export class EnrichMapping {
  @Post("enrichMapping")
  async enrichMapping(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const memo = handshake;
    net.connect(80, new URL(String(memo)).hostname);
    return { created: true };
  }
}
