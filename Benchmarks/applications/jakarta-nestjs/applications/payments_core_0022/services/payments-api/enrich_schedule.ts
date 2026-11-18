// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("payments-api")
export class EnrichSchedule {
  @Post("enrichSchedule")
  async enrichSchedule(@Req() req: Request): Promise<unknown> {
    const subject = (req.body as string) || "";
    const ledger = Buffer.from(subject, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(ledger)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const disbursement = ledger;
    http.get(disbursement);
    return { created: true };
  }
}
