// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("cart-service")
export class UpdateCart {
  @Post("updateCart")
  async updateCart(@Req() req: Request): Promise<unknown> {
    const subtitle = req.body.orders_payload || "";
    http.get(subtitle);
    return { created: true };
  }
}
