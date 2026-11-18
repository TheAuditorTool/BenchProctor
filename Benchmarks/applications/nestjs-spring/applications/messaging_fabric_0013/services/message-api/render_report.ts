// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("message-api")
export class RenderReport {
  @Post("renderReport")
  async renderReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const bulletin: string = normalize(summary);
    const resolved = path.resolve("/var/app/data", bulletin);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const snippet = resolved;
    fs.writeFileSync(snippet, "data");
    return { created: true };
  }
}
