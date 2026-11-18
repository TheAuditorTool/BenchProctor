// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("order-api")
export class BuildCheckpoint {
  @Post("buildCheckpoint")
  async buildCheckpoint(@Req() req: Request): Promise<unknown> {
    const memo = (req.query.id as string) || "";
    const voucher = Buffer.from(memo, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(voucher)) { throw new BadRequestException({error:"invalid"}); }
    const backorder = voucher;
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}
