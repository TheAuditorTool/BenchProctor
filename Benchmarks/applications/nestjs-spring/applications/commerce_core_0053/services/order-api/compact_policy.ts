// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("order-api")
export class CompactPolicy {
  @Post("compactPolicy/:id")
  async compactPolicy(@Req() req: Request): Promise<unknown> {
    const memo = (req.params.id as string) || "";
    const voucher = decodeURIComponent(memo);
    if (!/^(asc|desc|name|created)$/.test(String(voucher))) { throw new BadRequestException({error:"invalid"}); }
    const backorder = voucher;
    return "<div>" + backorder + "</div>";
  }
}
