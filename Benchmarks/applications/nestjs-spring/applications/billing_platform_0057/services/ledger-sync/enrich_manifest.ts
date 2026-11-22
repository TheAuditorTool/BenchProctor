// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("ledger-sync")
export class EnrichManifest {
  @Post("enrichManifest")
  async enrichManifest(@Req() req: Request): Promise<unknown> {
    const caption = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const remittance: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dunning = remittance;
    http.get(dunning);
    return { created: true };
  }
}
