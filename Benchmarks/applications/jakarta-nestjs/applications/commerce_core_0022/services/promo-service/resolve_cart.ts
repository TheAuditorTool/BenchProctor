// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("promo-service")
export class ResolveCart {
  @Post("resolveCart")
  async resolveCart(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers["x-custom-header"] as string) || "";
    const parts: string[] = [];
    for (const token of String(subject).split(',')) { parts.push(token); }
    const voucher: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(voucher))) { throw new BadRequestException({error:"invalid"}); }
    const backorder = voucher;
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}
