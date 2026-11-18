// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("capture-service")
export class BuildHeader {
  @Post("buildHeader")
  async buildHeader(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const ledger: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = ledger;
    net.connect(80, new URL(String(remittance)).hostname);
    return { created: true };
  }
}
