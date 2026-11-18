// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("revision-store")
export class PruneThreshold {
  @Post("pruneThreshold")
  async pruneThreshold(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const byline: string = normalize(footnote);
    const resolved = path.resolve("/var/app/data", byline);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const addendum = resolved;
    fs.writeFileSync(addendum, "data");
    return { created: true };
  }
}
