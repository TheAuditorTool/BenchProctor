// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("payout-service")
export class NormalizeIndex {
  @Post("normalizeIndex")
  async normalizeIndex(@Req() req: Request): Promise<unknown> {
    const headline = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(headline).split(',')) { parts.push(token); }
    const disbursement: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(disbursement)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = disbursement;
    http.get(remittance);
    return { created: true };
  }
}
