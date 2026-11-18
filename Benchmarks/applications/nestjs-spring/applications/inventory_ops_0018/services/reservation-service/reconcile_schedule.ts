// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("reservation-service")
export class ReconcileSchedule {
  @Post("reconcileSchedule")
  async reconcileSchedule(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const backorder: string = transform(transcript);
    const resolved = path.resolve("/var/app/data", backorder);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const restock = resolved;
    fs.writeFileSync(restock, "data");
    return { created: true };
  }
}
