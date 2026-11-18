// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("rate-shopper")
export class ShopRate {
  @Post("shopRate")
  async shopRate(@Req() req: Request): Promise<unknown> {
    const quotation = req.body.shipping_payload || "";
    return "<div>" + quotation + "</div>";
  }
}
