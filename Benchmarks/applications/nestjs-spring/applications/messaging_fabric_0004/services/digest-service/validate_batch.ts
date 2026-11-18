// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("digest-service")
export class ValidateBatch {
  @Post("validateBatch")
  async validateBatch(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(paragraph).split(',')) { parts.push(token); }
    const bulletin: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(bulletin)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const synopsis = bulletin;
    net.connect(80, new URL(String(synopsis)).hostname);
    return { created: true };
  }
}
