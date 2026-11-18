// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("fx-service")
export class ConvertFx {
  @Post("convertFx/:id")
  async convertFx(@Req() req: Request): Promise<unknown> {
    const subject = (req.params.id as string) || "";
    let ledger;
    try { ledger = JSON.parse(subject).value || subject; }
    catch (e) { ledger = subject; }
    await fetch("http://payments-api:8080/AuthorizePayment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
    return { created: true };
  }
}
