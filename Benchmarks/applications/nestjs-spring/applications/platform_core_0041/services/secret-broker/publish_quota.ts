// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("secret-broker")
export class PublishQuota {
  @Post("publishQuota")
  async publishQuota(@Req() req: Request): Promise<unknown> {
    const passage = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(passage).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const handshake = persona;
    http.get(handshake);
    return { created: true };
  }
}
