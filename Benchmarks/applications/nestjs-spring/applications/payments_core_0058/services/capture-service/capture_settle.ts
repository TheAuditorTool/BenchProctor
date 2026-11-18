// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("capture-service")
export class SettleCapture {
  @Post("settleCapture")
  async settleCapture(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const ledger = String(caption).replace(/\u0000/g, "");
    await fetch("http://payments-api:8080/AuthorizePayment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
    return { created: true };
  }
}
