// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("payout-service")
export class RotateConfig {
  @Post("rotateConfig")
  async rotateConfig(@Req() req: Request): Promise<unknown> {
    const memo = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(memo).split(',')) { parts.push(token); }
    const ledger: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = ledger;
    const outbound = { method: "get", url: String(remittance), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
