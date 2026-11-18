// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("supplier-feed")
export class CompactCheckpoint {
  @Post("compactCheckpoint")
  async compactCheckpoint(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    const tokens = String(citation).split(',').filter((t) => t.length > 0);
    const backorder = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(backorder))) { throw new BadRequestException({error:"invalid"}); }
    const restock = backorder;
    childProcess.execSync("echo " + restock);
    return { created: true };
  }
}
