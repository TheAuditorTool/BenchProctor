// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("cart-service")
export class ValidateOrder {
  @Post("validateOrder")
  async validateOrder(@Req() req: Request): Promise<unknown> {
    const memo = (req.body as string) || "";
    const voucher = Buffer.from(memo, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(voucher)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const backorder = voucher;
    http.get(backorder);
    return { created: true };
  }
}
