// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("order-history")
export class LookupOrder {
  @Post("lookupOrder")
  async lookupOrder(@Req() req: Request): Promise<unknown> {
    const summary = req.body.orders_payload || "";
    const resolved = path.resolve("/var/app/data", summary);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const voucher = resolved;
    fs.unlinkSync(voucher);
    return { created: true };
  }
}
