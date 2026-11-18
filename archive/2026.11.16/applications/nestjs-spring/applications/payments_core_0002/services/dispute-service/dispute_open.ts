// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("dispute-service")
export class OpenDispute {
  @Post("openDispute")
  async openDispute(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers.authorization as string) || "";
    const ledger = Buffer.from(subtitle, "base64").toString();
    await fetch("http://payments-api:8080/AuthorizePayment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
    return { created: true };
  }
}
