// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("dispute-service")
export class EnrichWallet {
  @Post("enrichWallet")
  async enrichWallet(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers.host as string) || "";
    const ledger = `${subtitle}`;
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = ledger;
    http.get(remittance);
    return { created: true };
  }
}
