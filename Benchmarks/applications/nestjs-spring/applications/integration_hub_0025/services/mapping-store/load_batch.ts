// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("mapping-store")
export class LoadBatch {
  @Post("loadBatch")
  async loadBatch(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(footnote);
    const resolved = path.resolve("/var/app/data", handshake);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const blurb = resolved;
    fs.writeFileSync(blurb, "data");
    return { created: true };
  }
}
