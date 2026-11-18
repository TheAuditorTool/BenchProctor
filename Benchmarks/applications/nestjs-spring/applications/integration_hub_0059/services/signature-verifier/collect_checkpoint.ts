// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("signature-verifier")
export class CollectCheckpoint {
  @Post("collectCheckpoint")
  async collectCheckpoint(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const memo = handshake;
    http.get(memo);
    return { created: true };
  }
}
