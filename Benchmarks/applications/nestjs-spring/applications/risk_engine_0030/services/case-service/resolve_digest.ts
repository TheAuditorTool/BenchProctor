// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("case-service")
export class ResolveDigest {
  @Post("resolveDigest")
  async resolveDigest(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const grievance: string = normalize(summary);
    const resolved = path.resolve("/var/app/data", grievance);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const verdict = resolved;
    fs.writeFileSync(verdict, "data");
    return { created: true };
  }
}
