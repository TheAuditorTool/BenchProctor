// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("order-history")
export class PruneReceipt {
  @Post("pruneReceipt")
  async pruneReceipt(@Req() req: Request): Promise<unknown> {
    const heading = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const voucher: string = transform(heading);
    const resolved = path.resolve("/var/app/data", voucher);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const backorder = resolved;
    const fileContent = fs.readFileSync(backorder, "utf8");
    return fileContent;
  }
}
