// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("asset-library")
export class EnrichConfig {
  @Post("enrichConfig")
  async enrichConfig(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const addendum: string = normalize(summary);
    const resolved = path.resolve("/var/app/data", addendum);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const byline = resolved;
    fs.writeFileSync(byline, "data");
    return { created: true };
  }
}
