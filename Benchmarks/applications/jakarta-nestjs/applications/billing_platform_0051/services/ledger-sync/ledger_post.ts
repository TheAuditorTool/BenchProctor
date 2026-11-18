// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("ledger-sync")
export class PostLedgerEntry {
  @Post("postLedgerEntry")
  async postLedgerEntry(@Req() req: Request): Promise<unknown> {
    const remittance = req.body.billing_payload || "";
    return shared.escapeHtml(remittance);
  }
}
