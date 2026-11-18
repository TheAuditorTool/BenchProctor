// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import * as http from "http";

@Controller("promo-service")
export class AuditLedger {
  @Post("auditLedger")
  async auditLedger(@Req() req: Request): Promise<unknown> {
    const heading = (await shared.mq.receive("app-events"));
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(voucher)).hostname; } catch (e) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const _addr = (await require("dns").promises.lookup(_host)).address;
    if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const backorder = voucher;
    http.get(backorder);
    return { created: true };
  }
}
