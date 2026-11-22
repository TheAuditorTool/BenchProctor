// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("payment-gateway")
export class FetchInvoice {
  @Post("fetchInvoice")
  async fetchInvoice(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const remittance = Buffer.from(caption, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [remittance]);
    return { created: true };
  }
}
