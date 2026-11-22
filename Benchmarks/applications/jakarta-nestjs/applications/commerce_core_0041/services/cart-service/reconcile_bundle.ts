// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("cart-service")
export class ReconcileBundle {
  @Post("reconcileBundle")
  async reconcileBundle(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["x-custom-header"] as string) || "";
    const parts: string[] = [];
    for (const token of String(headline).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(backorder))) { throw new BadRequestException({error:"invalid"}); }
    const voucher = backorder;
    childProcess.execSync("echo " + voucher);
    return { created: true };
  }
}
