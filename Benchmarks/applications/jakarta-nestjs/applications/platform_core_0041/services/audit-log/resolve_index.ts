// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("audit-log")
export class ResolveIndex {
  @Post("resolveIndex")
  async resolveIndex(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.multipart_field as string) || "";
    let persona;
    try { persona = JSON.parse(passage).value || passage; }
    catch (e) { persona = passage; }
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const _addr = (await require("dns").promises.lookup(_host)).address;
    if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const handshake = persona;
    http.get(handshake);
    return { created: true };
  }
}
