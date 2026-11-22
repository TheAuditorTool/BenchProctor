// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("ledger-sync")
export class PostLedgerEntry {
  @Post("postLedgerEntry")
  async postLedgerEntry(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const remittance = caption != null ? caption : '';
    await fetch("http://payment-gateway:8080/CapturePayment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
    return { created: true };
  }
}
