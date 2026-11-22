// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("payout-service")
export class SchedulePayout {
  @Post("schedulePayout")
  async schedulePayout(@Req() req: Request): Promise<unknown> {
    const headline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const disbursement: string = normalize(headline);
    await fetch("http://reconcile-service:8080/RunReconciliation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: disbursement})});
    return { created: true };
  }
}
