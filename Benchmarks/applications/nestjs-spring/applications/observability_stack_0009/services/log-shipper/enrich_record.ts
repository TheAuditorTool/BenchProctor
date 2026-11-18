// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("log-shipper")
export class EnrichRecord {
  @Post("enrichRecord")
  async enrichRecord(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const gauge: string = normalize(summary);
    const resolved = path.resolve("/var/app/data", gauge);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const cohort = resolved;
    fs.writeFileSync(cohort, "data");
    return { created: true };
  }
}
