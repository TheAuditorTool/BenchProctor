// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("promo-service")
export class FetchBatch {
  @Post("fetchBatch")
  async fetchBatch(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const voucher: string = transform(heading);
    const resolved = path.resolve("/var/app/data", voucher);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const backorder = resolved;
    fs.writeFileSync(backorder, "data");
    return { created: true };
  }
}
