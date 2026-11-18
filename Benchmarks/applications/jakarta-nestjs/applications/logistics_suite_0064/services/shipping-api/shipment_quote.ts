// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("shipping-api")
export class QuoteShipment {
  @Post("quoteShipment")
  async quoteShipment(@Req() req: Request): Promise<unknown> {
    const footnote = req.body.shipping_payload || "";
    return "<div>" + footnote + "</div>";
  }
}
