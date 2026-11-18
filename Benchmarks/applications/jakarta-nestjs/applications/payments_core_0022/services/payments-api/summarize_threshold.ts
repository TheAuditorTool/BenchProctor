// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("payments-api")
export class SummarizeThreshold {
  @Post("summarizeThreshold")
  async summarizeThreshold(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.origin as string) || "";
    const _input = String(subject);
    let ledger;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': ledger = _input.normalize('NFC'); break;
      default: ledger = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const disbursement = ledger;
    http.get(disbursement);
    return { created: true };
  }
}
