// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("cart-service")
export class CollectPolicy {
  @Post("collectPolicy")
  async collectPolicy(@Req() req: Request): Promise<unknown> {
    const memo = (req.body as string) || "";
    const voucher = String(memo).split(/[ \t]+/).join(" ");
    http.get(voucher);
    return { created: true };
  }
}
