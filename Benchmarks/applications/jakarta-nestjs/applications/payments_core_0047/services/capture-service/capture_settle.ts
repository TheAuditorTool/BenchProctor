// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("capture-service")
export class SettleCapture {
  @Post("settleCapture")
  async settleCapture(@Req() req: Request): Promise<unknown> {
    const ledger = req.body.payments_payload || "";
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(ledger)) { throw new BadRequestException({error:"invalid"}); }
    const disbursement = ledger;
    return new StreamableFile(Buffer.from("<section>" + disbursement + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
