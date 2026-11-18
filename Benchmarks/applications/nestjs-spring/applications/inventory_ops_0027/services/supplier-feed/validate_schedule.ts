// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("supplier-feed")
export class ValidateSchedule {
  @Post("validateSchedule")
  async validateSchedule(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    const restock = Buffer.from(summary, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(restock)) { throw new BadRequestException({error:"invalid"}); }
    const backorder = restock;
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}
