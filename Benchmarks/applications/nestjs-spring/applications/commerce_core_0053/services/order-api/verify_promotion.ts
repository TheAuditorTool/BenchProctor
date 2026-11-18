// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("order-api")
export class VerifyPromotion {
  @Post("verifyPromotion")
  async verifyPromotion(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["user-agent"] as string) || "";
    const tokens = String(memo).split(',').filter((t) => t.length > 0);
    const voucher = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(voucher))) { throw new BadRequestException({error:"invalid"}); }
    const backorder = voucher;
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}
