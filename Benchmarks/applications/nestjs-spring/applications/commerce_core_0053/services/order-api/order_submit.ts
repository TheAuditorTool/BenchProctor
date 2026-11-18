// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("order-api")
export class PlaceOrder {
  @Post("placeOrder")
  async placeOrder(@Req() req: Request): Promise<unknown> {
    const memo = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const parts: string[] = [];
    for (const token of String(memo).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    await fetch("http://cart-service:8080/UpdateCart", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
    return { created: true };
  }
}
