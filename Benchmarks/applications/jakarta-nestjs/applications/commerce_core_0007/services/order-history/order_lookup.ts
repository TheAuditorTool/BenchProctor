// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("order-history")
export class LookupOrder {
  @Post("lookupOrder")
  async lookupOrder(@Req() req: Request): Promise<unknown> {
    const wording = req.body.orders_payload || "";
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(wording)) { throw new BadRequestException({error:"invalid"}); }
    const backorder = wording;
    return "<div>" + backorder + "</div>";
  }
}
