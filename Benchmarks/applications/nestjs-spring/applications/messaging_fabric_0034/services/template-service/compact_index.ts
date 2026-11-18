// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("template-service")
export class CompactIndex {
  @Post("compactIndex")
  async compactIndex(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(footnote);
    const bulletin: string = readInput();
    let _host = "";
    try { _host = new URL(String(bulletin)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const heading = bulletin;
    http.get(heading);
    return { created: true };
  }
}
