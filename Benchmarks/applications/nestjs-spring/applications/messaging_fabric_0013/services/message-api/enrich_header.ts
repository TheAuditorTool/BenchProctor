// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("message-api")
export class EnrichHeader {
  @Post("enrichHeader")
  async enrichHeader(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const bulletin: string = readInput();
    let _host = "";
    try { _host = new URL(String(bulletin)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const snippet = bulletin;
    http.get(snippet);
    return { created: true };
  }
}
