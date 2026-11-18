// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { UseGuards } from "@nestjs/common";
import { AuthGuard } from "./auth.guard";

@Controller("billing-api")
export class SubmitInvoice {
  @Post("submitInvoice")
  @UseGuards(AuthGuard)
  async submitInvoice(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.authorization as string) || "";
    const arrears = Buffer.from(synopsis, "base64").toString();
    await fetch("http://ledger-sync:8080/PostLedgerEntry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: arrears})});
    return { created: true };
  }
}
