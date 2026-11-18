// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("order-history")
export class LookupOrder {
  @Post("lookupOrder")
  async lookupOrder(@Req() req: Request): Promise<unknown> {
    const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const parts: string[] = [];
    for (const token of String(citation).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    await fetch("http://returns-service:8080/RequestReturn", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
    return { created: true };
  }
}
